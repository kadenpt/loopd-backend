from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import FollowCreate, FollowResponse
from app.services.follow_service import (
  create_follow as create_follow_service,
  get_follows as get_follows_service,
  remove_follow as remove_follow_service
)

router = APIRouter(prefix="/follow", tags=["Follow"])

@router.post("/{user_id}", response_model=FollowResponse, description="Create a follow relationship")
def create_follow(follower_id: int, followed_id: int, db: Session = Depends(get_db)):
    return create_follow_service(db, follower_id, followed_id)

@router.get("/{user_id}", response_model=list[FollowResponse], description="Get all follows for a user")
def get_follows(user_id: int, db: Session = Depends(get_db)):
    return get_follows_service(db, user_id)

@router.delete("/{user_id}", description="Remove a follow relationship")
def remove_follow(follower_id: int, followed_id: int, db: Session = Depends(get_db)):
    return remove_follow_service(db, follower_id, followed_id)