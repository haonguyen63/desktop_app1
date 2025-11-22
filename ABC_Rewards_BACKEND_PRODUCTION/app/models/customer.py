
from sqlalchemy import Column,String,Integer
from app.db.base import Base

class Customer(Base):
    __tablename__="customers"
    id=Column(Integer,primary_key=True)
    phone=Column(String,unique=True,index=True)
    name=Column(String)
    points=Column(Integer,default=0)
