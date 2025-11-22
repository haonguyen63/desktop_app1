
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.customer import CustomerOut
from app.db.session import get_db
from app.models.customer import Customer

router=APIRouter()

@router.get("/{phone}",response_model=CustomerOut)
def find_or_create(phone:str,db:Session=Depends(get_db)):
    c=db.query(Customer).filter(Customer.phone==phone).first()
    if not c:
        c=Customer(phone=phone,name="Khách mới",points=0)
        db.add(c); db.commit(); db.refresh(c)
    return c
