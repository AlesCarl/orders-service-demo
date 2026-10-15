from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 2
    assert body[0] == {"id": 1, "customer": "Mario Rossi", "amount": "49.90"}
