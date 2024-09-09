from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import settings

sync_engine = create_engine(settings.sync_url, echo=True)
async_engine = create_async_engine(settings.async_url, echo=True)

sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    ...