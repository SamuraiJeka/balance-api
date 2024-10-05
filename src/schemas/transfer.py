from pydantic import BaseModel, PositiveInt


class Transfer(BaseModel):
    id: int
    recipient_id: int
    amount: PositiveInt
