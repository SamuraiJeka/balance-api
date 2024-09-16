from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from db.config import settings

async_engine = create_async_engine(settings.async_url, echo=True)

async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    ...
