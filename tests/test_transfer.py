from httpx import AsyncClient


async def test_transfer(ac: AsyncClient):
    body = {
        "id": 1,
        "recipient_id": 2,
        "amount": 400
    }
    response = await ac.post("/balance/c", json=body)

    assert response.status_code == 200
    assert response.json() == {"result": "Successful transfer"}


async def test_incorrect_transfer(ac: AsyncClient):
    body = {
        "id": 1,
        "recipient_id": 2,
        "amount": -400
    }
    response = await ac.post("/balance/transfer", json=body)

    assert response.status_code == 422
