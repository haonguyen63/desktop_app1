
from pydantic import BaseModel

class CustomerOut(BaseModel):
    phone:str
    name:str
    points:int
    class Config:
        orm_mode=True
