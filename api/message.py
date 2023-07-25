
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response

from .schemas import MessageRequest, MessageResponse
from .repositories import MessageRepository, StatisticRepository
from .database import get_db
from .models import Message

router = APIRouter()

@router.get("/", response_model=list[MessageResponse])
def show_message(db:Session = Depends(get_db)):
    records = MessageRepository.find_all(db)
    return records

@router.post("/",response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def create_message(request: MessageRequest, db: Session = Depends(get_db)):
    curso = MessageRepository.save(db, Message(**request.model_dump()))
    # add a message in statistic's table
    StatisticRepository.exists_customer_type_date(db, curso)
    return MessageResponse.model_validate(curso)