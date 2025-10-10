from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Follow
from app.schemas import FollowCreate

def create_follow(db: Session, follower_id: int, followed_id: int):
    if follower_id == followed_id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")
    
    existing = (
      db.query(Follow).filter(
        Follow.follower_id == follower_id,
        Follow.followed_id == followed_id
      ).first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="You already follow this user")
    
    db_follow = Follow(follower_id=follower_id, followed_id=followed_id)
    db.add(db_follow)
    db.commit()
    db.refresh(db_follow)
    return db_follow

def get_follows(db: Session, user_id: int):
    follows = (
      db.query(Follow).filter(
        Follow.followed_id == user_id
      ).all()
    )
    return follows

def remove_follow(db: Session, follower_id: int, followed_id: int):
    follow = (
      db.query(Follow).filter(
        Follow.follower_id == follower_id,
        Follow.followed_id == followed_id
      ).first()
    )
    if not follow:
        raise HTTPException(status_code=404, detail="Follow not found")
    db.delete(follow)
    db.commit()
    return {"detail": "Follow removed successfully"}