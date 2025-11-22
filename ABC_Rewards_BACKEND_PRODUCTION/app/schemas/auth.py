
from pydantic import BaseModel

class Login(BaseModel):
    phone:str
    password:str

class Token(BaseModel):
    access_token:str
    refresh_token:str
    token_type:str="bearer"
