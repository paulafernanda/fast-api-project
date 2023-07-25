from sqlalchemy import Column, Integer, String, Float, Date
from fastapi_utils.guid_type import GUID
import uuid
from datetime import date

from .database import Base

class Message(Base):
    __tablename__ = "Messages"

    id: int = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, default=uuid.uuid4)
    customerId: int = Column(Integer, nullable=False)
    type: str = Column(String(255), nullable=False)
    amount: float = Column(Float, nullable=False)
    createdAt = Column(Date, default=date.today())

class Statistic(Base):
    __tablename__ = "Statistics"

    id: int = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, default=uuid.uuid4)
    customerId: int = Column(Integer, nullable=False)
    type: str = Column(String(255), nullable=False)
    message_count: int = Column(Integer, nullable=False)
    total_amount: float = Column(Float, nullable=False)
    start_date = Column(Date, default=date.today())