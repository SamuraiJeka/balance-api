from fastapi import APIRouter
from sqlalchemy import text
from config.db_session import async_session

from schemas.replenishment import Replenishment
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
        return {"result": "Error"}
    else:
        return{"result": "Balance replenished"}
    
