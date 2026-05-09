from typing import Any

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    """Generic request contract for model inference."""

    input_data: dict[str, Any] = Field(..., description="Input payload for model inference")


class PredictionResponse(BaseModel):
    """Generic response contract for model inference."""

    output: dict[str, Any] = Field(..., description="Model output payload")
    model_version: str = Field(..., description="Served model version")
