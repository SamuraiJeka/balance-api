from sqlalchemy import text
from db.session import async_session


async def get_version() -> None:
    async with async_session() as session:
        query = text("SELECT VERSION()")
        result = await session.execute(query)
    print(result.all())
