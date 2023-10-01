from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

# Schema/Pydantic models define the structure of a request & response


# Schemas for posts
# Input request schemas
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):
    pass


# Schemas for users
# for a library for email: from pydantic import BaseModel, EmailStr
# for request
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# for response
class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# Output post response schemas
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: User

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int


# For user Authentication
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserSession(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


# for tokens
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str


# for vote
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # less than or equal to 1
