from typing import Any

from src.models.stt_stream_adapter import SttStreamAdapter


class StreamingTranscriptionService:
    """Session-level orchestration for websocket transcription streams."""

    def __init__(self) -> None:
        self.adapter: SttStreamAdapter | None = None
        self.started = False

    async def start(self, language: str = "en") -> None:
        self.adapter = SttStreamAdapter(language=language)
        self.started = True

    async def handle_chunk(self, seq: int, audio_b64: str) -> dict[str, Any]:
        if not self.started or self.adapter is None:
            raise RuntimeError("Session not started. Send session_start first.")
        return await self.adapter.push_audio(seq=seq, audio_b64=audio_b64)

    async def end(self) -> str | None:
        final_text: str | None = None
        if self.adapter is not None:
            final_text = await self.adapter.close()
        self.adapter = None
        self.started = False
        return final_text
