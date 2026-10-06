from fastapi import FastAPI
from pydantic import BaseModel

from .agent import Agent

app = FastAPI(title="AI Agent API", version="0.1.0")
agent = Agent()

class CalculateRequest(BaseModel):
    expression: str

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/tools/calculate")
def calculate(request: CalculateRequest) -> dict[str, float | int]:
    return {"result": agent.run("calculate", expression=request.expression)}
