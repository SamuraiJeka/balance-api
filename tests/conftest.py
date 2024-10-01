import pytest
import os
import asyncio
from asyncio import AbstractEventLoop
from dotenv import load_dotenv
from typing import AsyncGenerator, Generator, Any
from httpx import AsyncClient
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool

from src.config.db_session import Base
from src.main import app


load_dotenv()

HOST = os.environ.get("DB_HOST_TEST")
PORT = os.environ.get("DB_PORT_TEST")
USER = os.environ.get("DB_USER_TEST")
PASSWORD = os.environ.get("DB_PASSWORD_TEST")
NAME = os.environ.get("DB_NAME_TEST")

DB_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}" 

engine_test = create_async_engine(DB_URL, poolclass=NullPool)
session_test = async_sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(autouse=True, scope="session")
async def setup():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def create_model():
    from src.models.person import Person
    async with session_test() as session:
        session.add(Person(id=1, balance=1000))
        await session.commit()


@pytest.fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, Any, None]:
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://balance") as ac:
        yield ac