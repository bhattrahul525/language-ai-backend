from typing import Literal, Optional
from pydantic import BaseModel

class SessionStart(BaseModel):
    type: Literal["session_start"]
    language: str = "en"


class AudioChunk(BaseModel):
    type: Literal["audio_chunk"]
    seq: int
    audio_b64: str  # base64 audio chunk


class SessionEnd(BaseModel):
    type: Literal["session_end"]


class PartialText(BaseModel):
    type: Literal["partial_text"]
    seq: int
    text: str


class FinalText(BaseModel):
    type: Literal["final_text"]
    text: str


class WsError(BaseModel):
    type: Literal["error"]
    message: str
    seq: Optional[int] = None