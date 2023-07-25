from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import NewType
from uuid import UUID

TypeID = NewType("TypeID", UUID)
TypeDate = NewType("TypeDate", date)

class MessageBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    customerId: int
    type: str
    amount: float

class MessageRequest(MessageBase):
    ...

class MessageResponse(MessageBase):
    id: int
    uuid: TypeID
    createdAt: TypeDate

    class Config:
        from_attributes = True
        population_by_name = True

class Statistic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    customerId: int
    type: str
    message_count: int
    total_amount: float

class StatisticRequest(Statistic):
    ...

class StatisticResponse(Statistic):
    id: int
    start_date: TypeDate

    class Config:
        from_attributes = True
        population_by_name = True