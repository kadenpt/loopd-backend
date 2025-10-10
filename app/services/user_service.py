from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_data: UserCreate):
    hashed_password = pwd_context.hash(user_data.password[:72])
    db_user = User(name=user_data.name, email=user_data.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    users = db.query(User).all()
    return users