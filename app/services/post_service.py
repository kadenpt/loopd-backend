from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Post
from app.schemas import PostCreate

def create_post(db: Session, post_data: PostCreate):
    db_post = Post(**post_data.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post  

def get_posts_by_user_id(db: Session, user_id: int):
    posts = db.query(Post).filter(Post.author_id == user_id).all()
    return posts

def update_post(db: Session, user_id: int, post_id: int, post_data: PostCreate):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Optional: ensure only the owner can update
    if post.author_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")

    post.content = post_data.content
    if post_data.photo_url:
      post.photo_url = post_data.photo_url

    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, user_id: int, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}