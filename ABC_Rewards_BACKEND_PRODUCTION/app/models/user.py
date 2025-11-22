
from sqlalchemy import Column,String,Integer
from app.db.base import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    phone=Column(String,unique=True,index=True)
    name=Column(String)
    role=Column(String)
    password_hash=Column(String)
