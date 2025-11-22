
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.transaction import TransactionCreate
from app.db.session import get_db
from app.models.transaction import Transaction
from app.models.customer import Customer

router=APIRouter()

@router.post("/create")
def create(data:TransactionCreate,db:Session=Depends(get_db)):
    c=db.query(Customer).filter(Customer.phone==data.phone).first()
    if not c: return {"error":"customer_not_found"}

    if data.action=="earn": c.points+=data.points
    if data.action=="redeem": c.points-=data.points

    t=Transaction(customer_phone=data.phone,staff_phone="staff",
                  action=data.action,amount=data.amount,points=data.points)
    db.add(t); db.commit()
    return {"status":"ok"}
