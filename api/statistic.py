
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from datetime import date

from .schemas import StatisticResponse
from .database import get_db
from .models import Statistic
from .repositories import StatisticRepository

router = APIRouter()

@router.get("/all", response_model=list[StatisticResponse])
def show_statistic(db:Session = Depends(get_db)):
    records = db.query(Statistic).all()
    return records

@router.get("/")
async def get_statistic(start_date: date, end_date:date, customerId:int, type:str, db: Session = Depends(get_db)):
    record = StatisticRepository.filter_date(db, start_date, end_date, customerId, type)
    return record
