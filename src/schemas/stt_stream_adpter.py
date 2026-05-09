class SttStreamAdapter:

    def __init__(self, language: str = "en"):
        self.language = language

    async def push_audio(self, seq: int, audio_bytes: bytes) -> dict:
        return {"partial": "", "final": None}

    async def close(self) -> None:
        return None