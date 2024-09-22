from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_calculate():
    response = client.get("/balance/replenishment")
    