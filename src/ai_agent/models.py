from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    session_id: str = "default"

class ChatResponse(BaseModel):
    session_id: str
    response: str
    tool_calls: list[str] = []

class ToolCall(BaseModel):
    name: str
    arguments: dict
