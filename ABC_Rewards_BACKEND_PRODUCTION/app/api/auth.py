
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import Login,Token
from app.core.security import verify,create_access_token,create_refresh_token
from app.db.session import get_db
from app.crud.user import get_by_phone

router=APIRouter()

@router.post("/login",response_model=Token)
def login(data:Login,db:Session=Depends(get_db)):
    user=get_by_phone(db,data.phone)
    if not user or not verify(data.password,user.password_hash):
        raise HTTPException(401,"Invalid login")
    access=create_access_token({"sub":user.phone,"role":user.role})
    refresh=create_refresh_token({"sub":user.phone})
    return Token(access_token=access,refresh_token=refresh)
