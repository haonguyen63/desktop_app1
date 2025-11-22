
from sqlalchemy import Column,Integer,String,DateTime,func
from app.db.base import Base

class Transaction(Base):
    __tablename__="transactions"
    id=Column(Integer,primary_key=True)
    customer_phone=Column(String,index=True)
    staff_phone=Column(String)
    action=Column(String)
    amount=Column(Integer)
    points=Column(Integer)
    created_at=Column(DateTime,server_default=func.now())
