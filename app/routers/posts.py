from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, schemas
from app.services.post_service import (
  create_post as create_post_service,
  get_posts_by_user_id as get_posts_by_user_id_service,
  update_post as update_post_service,
  delete_post as delete_post_service
)

router = APIRouter(prefix="/posts", tags=["Posts"])

get_db = database.get_db

@router.post(
    "/", 
    response_model=schemas.Post,
    description="Create a new post"
)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return create_post_service(db, post)

@router.get(
    "/{user_id}", 
    response_model=list[schemas.Post],
    description="Get all posts for a user"
)
def get_posts(user_id: int, db: Session = Depends(get_db)):
    posts = get_posts_by_user_id_service(db, user_id)
    return posts

@router.put(
  "/{post_id}",
  response_model=schemas.Post,
  description="Update a post"
)
def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    return update_post_service(db, post.author_id, post_id, post)

@router.delete(
  "/{post_id}",
  response_model=schemas.Post,
  description="Delete a post"
)
def delete_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    return delete_post_service(db, post.author_id, post_id)
