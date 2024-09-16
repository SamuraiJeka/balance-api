from fastapi import APIRouter
from sqlalchemy import text
from config.db_session import async_session


router = APIRouter(prefix="/balance", tags=["balance"])


@router.get("/version")
async def get_version() -> None:
    async with async_session() as session:
        query = text("SELECT VERSION()")
        result = await session.execute(query)
    return {"version": result.scalars().one()}
