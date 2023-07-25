from sqlalchemy.orm import Session
from datetime import date

from .models import Message, Statistic

class MessageRepository:
    @staticmethod
    def find_all(db: Session) -> list[Message]:
        return db.query(Message).all()

    @staticmethod
    def save(db: Session, message: Message) -> Message:
        if message.id:
            db.merge(message)
        else:
            db.add(message)
        db.commit()
        return message

class StatisticRepository:
  
    def exists_customer_type_date(db: Session, message: Message):
        # find if the exists a objetc in a Statistic's tables with the same customerId, type and date
        instance = db.query(Statistic).filter(Statistic.customerId == message.customerId, Statistic.type == message.type, Statistic.start_date == message.createdAt).first()

        if instance:
            # update the object Statistic
            instance.message_count += 1
            instance.total_amount += float(message.amount) 
            db.merge(instance)
        else:
            # add a new object to Statistic
            instance = Statistic(customerId = message.customerId, type = message.type, message_count = 1, total_amount = float(message.amount))
            db.add(instance)
        db.commit()
        return instance

    def filter_date(db:Session, start_date:date, end_date:date, customerId:int, type:str):
        # find all the objects with the same customerId and type in a range of dates
        instance = db.query(Statistic).filter(Statistic.start_date >= start_date, Statistic.start_date <= end_date, Statistic.customerId == customerId, Statistic.type == type)

        # sum all the objetcs find in the interval
        total_amount = sum(obj.total_amount for obj in instance)
        total_quantity = sum(obj.message_count for obj in instance)
        
        # return the result
        return {'customerId': customerId, 'type': type, 'total_amount': total_amount, 'message_count': total_quantity, 'start_date': start_date, 'end_date': end_date}


