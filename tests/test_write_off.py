from httpx import AsyncClient

async def test_minus_balance(ac: AsyncClient):
    body = {
        "id": 1,
        "amount": 100
    }
    response = await ac.post("/balance/write_off", json=body)

    assert response.status_code == 200
    assert response.json() == {"result": "Balance sheet write-off"}


async def test_incorrect_minus_balance(ac: AsyncClient):
    body = {
        "id": 1,
        "amount": -100
    }
    response = await ac.post("/balance/write_off", json=body)

    assert response.status_code == 422
