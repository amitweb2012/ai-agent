from fastapi import FastAPI
from pydantic import BaseModel

from .agent import Agent
from .models import ChatRequest, ChatResponse

app = FastAPI(title="Enterprise AI Agent", version="0.2.0")
agent = Agent()

class CalculateRequest(BaseModel):
    expression: str

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    response, tool_calls = agent.chat(request.session_id, request.message)
    return ChatResponse(session_id=request.session_id, response=response, tool_calls=tool_calls)

@app.post("/tools/calculate")
def calculate(request: CalculateRequest) -> dict[str, float | int]:
    return {"result": agent.run("calculate", expression=request.expression)}
