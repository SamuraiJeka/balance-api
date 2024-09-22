from pydantic import BaseModel


class Replenishment(BaseModel):
    id: int
    amount: int