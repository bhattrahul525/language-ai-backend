from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    """Basic liveliness probe for BE or orchestrator checks."""
    return {"status": "ok"}
