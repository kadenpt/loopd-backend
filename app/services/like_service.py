from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Like

def like_post(db: Session, user_id: int, post_id: int):
    existing = (
      db.query(Like).filter(
        Like.user_id == user_id,
        Like.post_id == post_id
      ).first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="You already liked this post")
    db_like = Like(user_id=user_id, post_id=post_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def unlike_post(db: Session, user_id: int, post_id: int):
    existing = (
      db.query(Like).filter(
        Like.post_id == post_id
      ).first()
    )
    if not existing:
        raise HTTPException(status_code=404, detail="Like not found")
    db.delete(existing)
    db.commit()
    return {"detail": "Unlike successful"}

def get_likes(db: Session, post_id: int):
    likes = (
      db.query(Like).filter(
        Like.post_id == post_id
      ).all()
    )
    return likes