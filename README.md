# language-ai-backend

Backend API and service orchestration repository.

This repository contains the backend architecture layers moved out of `language-ai-ml`:
- FastAPI app wiring and routers
- Service orchestration
- API/data schemas
- App settings/config

## Run locally

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8080
```

## Endpoints

- `GET /v1/health`
- `POST /v1/predict`
- `WS /v1/ws/transcribe`