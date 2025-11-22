
from pydantic import BaseModel

class TransactionCreate(BaseModel):
    phone:str
    action:str
    amount:int
    points:int
