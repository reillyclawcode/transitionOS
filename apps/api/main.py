from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TransitionOS API", version="0.0.1")


class HealthResponse(BaseModel):
    status: str = "ok"
    service: str = "transitionos-api"


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse()


@app.get("/v1/runs")
async def list_runs():
    """Placeholder hook the dashboard can call until real data exists."""
    return {"runs": []}
