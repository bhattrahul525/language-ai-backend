from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.services.streaming_transcription import StreamingTranscriptionService

router = APIRouter(tags=["websocket-transcription"])


@router.websocket("/ws/transcribe")
async def ws_transcribe(websocket: WebSocket) -> None:
    await websocket.accept()
    service = StreamingTranscriptionService()

    try:
        while True:
            event = await websocket.receive_json()
            event_type = event.get("type")

            if event_type == "session_start":
                language = event.get("language", "en")
                await service.start(language=language)
                await websocket.send_json({"type": "ack", "message": "session_started"})
                continue

            if event_type == "audio_chunk":
                seq = int(event.get("seq", 0))
                audio_b64 = event.get("audio_b64", "")
                result = await service.handle_chunk(seq=seq, audio_b64=audio_b64)

                if result.get("text"):
                    await websocket.send_json({"type": "text", "seq": result["seq"], "text": result["text"]})
                continue

            if event_type == "session_end":
                final_text = await service.end()
                if final_text:
                    await websocket.send_json({"type": "text", "text": final_text})
                await websocket.send_json({"type": "ack", "message": "session_ended"})
                break

            await websocket.send_json({"type": "error", "message": f"Unknown event type: {event_type}"})
    except WebSocketDisconnect:
        await service.end()
    except Exception as exc:  # noqa: BLE001
        await service.end()
        await websocket.send_json({"type": "error", "message": str(exc)})
