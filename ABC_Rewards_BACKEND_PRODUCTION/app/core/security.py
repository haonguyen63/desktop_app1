
from datetime import datetime,timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY="SUPERSECRET"
REFRESH_SECRET="REFRESHSECRET"
ALGO="HS256"

pwd=CryptContext(schemes=["bcrypt"])

def hash_password(p): return pwd.hash(p)
def verify(p,h): return pwd.verify(p,h)

def create_access_token(data:dict):
    to=data.copy(); to["exp"]=datetime.utcnow()+timedelta(minutes=15)
    return jwt.encode(to,SECRET_KEY,ALGO)

def create_refresh_token(data:dict):
    to=data.copy(); to["exp"]=datetime.utcnow()+timedelta(days=30)
    return jwt.encode(to,REFRESH_SECRET,ALGO)
