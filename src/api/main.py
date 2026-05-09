from fastapi import FastAPI

from src.api.routers.health import router as health_router
from src.api.routers.infer import router as infer_router
from src.api.routers.ws_transcribe import router as ws_transcribe_router


def create_app() -> FastAPI:
    """Build and configure the base ML service API application."""
    app = FastAPI(title="ML Service", version="0.1.0")
    app.include_router(health_router, prefix="/v1")
    app.include_router(infer_router, prefix="/v1")
    app.include_router(ws_transcribe_router, prefix="/v1")
    return app


app = create_app()
