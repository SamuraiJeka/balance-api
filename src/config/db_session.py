from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config.db_config import settings

async_engine = create_async_engine(settings.async_url, echo=True)

async_session = async_sessionmaker(async_engine)

metadata = MetaData()

class Base(DeclarativeBase):
    ...
