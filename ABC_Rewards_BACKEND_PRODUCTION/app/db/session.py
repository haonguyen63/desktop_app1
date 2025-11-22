
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.core.security import hash_password
from app.models.user import User

DATABASE_URL="postgresql://neondb_owner:npg_v3TGmcLtU6fx@ep-plain-cherry-a44f8xsc-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    db=SessionLocal()
    if not db.query(User).first():
        admin=User(phone="admin",name="Admin",role="admin",
                   password_hash=hash_password("admin"))
        db.add(admin); db.commit()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
