from httpx import AsyncClient
from conftest import session_test


async def test_sum_balance(ac: AsyncClient):
    body = {
        "id": 1,
        "amount": 100
    }
    response = await ac.post("/balance/replenishment", json=body)

    assert response.status_code == 200
    assert response.json() == {"result": "Balance replenished"}


async def test_string_sum_balance(ac: AsyncClient):
    body = {
        "id": 1,
        "amount": "100"
    }
    response = await ac.post("/balance/replenishment", json=body)

    assert response.status_code == 200
    assert response.json() == {"result": "Balance replenished"}
    