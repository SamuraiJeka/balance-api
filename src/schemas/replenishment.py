from pydantic import BaseModel, PositiveInt


class Replenishment(BaseModel):
    id: int
    amount: PositiveInt