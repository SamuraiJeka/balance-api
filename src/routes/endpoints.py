from fastapi import APIRouter
from config.db_session import async_session

from schemas.replenishment import Replenishment
from schemas.write_off import Write_off
from schemas.transfer import Transfer

from models.person import Person


router = APIRouter(prefix="/balance", tags=["balance"])


@router.post("/replenishment")
async def replenishment(replenishment: Replenishment):
    try:
        async with async_session() as session:
            user = await session.get(Person, replenishment.id)
            user.balance += replenishment.amount
            await session.commit()
    except:
        return {"result": "Server error"}
    else:
        return {"result": "Balance replenished"}


@router.post("/write_off")
async def write_off(write_off: Write_off):
    try:
        async with async_session() as session:
            user = await session.get(Person, write_off.id)
            if user.balance - write_off.amount < 0:
                return {"result": "Insufficient funds "}
            user.balance -= write_off.amount
            await session.commit()
    except:
        return {"result": "Server error"}
    else:
        return {"result": "Balance sheet write-off"}


@router.post("/transfer")
async def transfer(transfer: Transfer):
    try:
        async with async_session() as session:
            sender = await session.get(Person, transfer.id)
            recipient = await session.get(Person, transfer.recipient_id)
            if sender.balance < transfer.amount:
                return {"result": "Underdraft"}
            sender.balance -= transfer.amount
            recipient.balance += transfer.amount
            await session.commit()
    except:
        return {"result": "Server error"}
    else:
        return {"result": "Successful transfer"}
