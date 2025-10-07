from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database
from app import schemas
from app import models
from app.models import User
from app.schemas import UserCreate
from app.database import SessionLocal
from app.services.user_service import (
  create_user as create_user_service,
  get_users as get_users_service
)

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)

@router.get("/", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
      users = get_users_service(db)
      if not users:
          raise HTTPException(status_code=404, detail="No users found")
      return users
