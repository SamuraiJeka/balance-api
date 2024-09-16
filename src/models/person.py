from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger
from config.db_session import Base


class Person(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(BigInteger(), default=0, nullable=False)
