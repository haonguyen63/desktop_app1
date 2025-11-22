from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.customer import router as customer_router
from app.api.transaction import router as transaction_router
from app.db.session import init_db

app=FastAPI(title="ABC Rewards Backend")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"status": "Backend running OK"}

app.include_router(auth_router,prefix="/auth",tags=["auth"])
app.include_router(customer_router,prefix="/customer",tags=["customer"])
app.include_router(transaction_router,prefix="/transaction",tags=["transaction"])
