from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from session import sync_engine, async_session
from sqlalchemy import text, select, BigInteger
from session import Base



class Person(Base):
    __tablename__="persons"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(BigInteger(), default=0, nullable=False)
