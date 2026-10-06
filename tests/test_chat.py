from fastapi.testclient import TestClient
from ai_agent.api import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat", json={"message": "hello", "session_id": "test"})
    assert response.status_code == 200
    assert response.json()["session_id"] == "test"
