import base64
from typing import Any

from src.models.speech_to_text.SpeechToText import SpeechToText


class SttStreamAdapter:
    """
    Streaming STT adapter placeholder.
    Replace this implementation with a real provider SDK integration.
    """

    def __init__(self, language: str = "en") -> None:
        self.language = language
        self._last_text = ""
        self._audio_buffer = bytearray()
        self._chunk_count = 0
        self._engine = SpeechToText()

    async def push_audio(self, seq: int, audio_b64: str) -> dict[str, Any]:
        """
        Consume an audio chunk and return partial/final transcript events.
        Current stub emits predictable text so FE/BE can verify socket flow.
        """
        audio_bytes = base64.b64decode(audio_b64) if audio_b64 else b""
        if not audio_bytes:
            return {"text": "", "seq": seq}

        # Accumulate chunks so transcription has enough context to capture
        # more than a single token from short slices.
        self._audio_buffer.extend(audio_bytes)
        self._chunk_count += 1

        emit_text = self._chunk_count % 4 == 0
        if not emit_text:
            return {"text": "", "seq": seq}

        transcript = self._engine.transcribe_audio_bytes(audio_bytes=bytes(self._audio_buffer))
        if not transcript:
            return {"text": "", "seq": seq}

        if transcript.startswith(self._last_text):
            text_delta = transcript[len(self._last_text):].strip()
        else:
            text_delta = transcript.strip()

        self._last_text = transcript
        return {"text": text_delta, "seq": seq}

    async def close(self) -> str | None:
        final_text: str | None = None
        if self._audio_buffer:
            transcript = self._engine.transcribe_audio_bytes(audio_bytes=bytes(self._audio_buffer))
            if transcript:
                if transcript.startswith(self._last_text):
                    final_text = transcript[len(self._last_text):].strip() or None
                elif transcript != self._last_text:
                    final_text = transcript

        self._audio_buffer = bytearray()
        self._chunk_count = 0
        self._last_text = ""
        return final_text
