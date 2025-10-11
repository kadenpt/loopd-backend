from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.database import get_db
from app.schemas import LikeCreate, LikeResponse
from app.services.like_service import (
    like_post as like_post_service,
    unlike_post as unlike_post_service,
    get_likes as get_likes_service
)

router = APIRouter(prefix="/likes", tags=["Likes"])

@router.post("/{post_id}", response_model=LikeResponse, description="Like a post")
def like_post(user_id: int, post_id: int, db: Session = Depends(get_db)):
    return like_post_service(db, user_id, post_id)

@router.delete("/{post_id}", description="Unlike a post")
def unlike_post(user_id: int, post_id: int, db: Session = Depends(get_db)):
    return unlike_post_service(db, user_id, post_id)

@router.get("/{post_id}", response_model=list[LikeResponse], description="Get all likes for a post")
def get_likes(post_id: int, db: Session = Depends(get_db)):
    return get_likes_service(db, post_id)
