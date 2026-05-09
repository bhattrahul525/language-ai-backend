from fastapi import APIRouter

from src.schemas.prediction import PredictionRequest, PredictionResponse
from src.services.inference import run_inference

router = APIRouter(tags=["inference"])


@router.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest) -> PredictionResponse:
    """Generic prediction endpoint for internal BE calls."""
    result = run_inference(payload.input_data)
    return PredictionResponse(output=result["output"], model_version=result["model_version"])
