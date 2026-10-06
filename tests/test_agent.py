from fastapi.testclient import TestClient

from ai_agent.api import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_calculate_api():
    response = client.post("/tools/calculate", json={"expression": "(10 + 5) * 2"})
    assert response.status_code == 200
    assert response.json() == {"result": 30}
