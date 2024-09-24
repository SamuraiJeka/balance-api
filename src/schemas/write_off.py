from pydantic import BaseModel, PositiveInt


class Write_off(BaseModel):
    id: int
    amount: PositiveInt
