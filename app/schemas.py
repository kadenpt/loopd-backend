from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    content: str
    photo_url: Optional[str] = None

class PostCreate(PostBase):
    author_id: int

class Post(PostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

class Follow(BaseModel):
    follower_id: int
    followed_id: int

class FollowCreate(Follow):
    pass

class FollowResponse(Follow):
    id: int

    class Config:
        from_attributes = True