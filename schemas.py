from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    user_id: int = 1
    category_id: int = 1
    subcategory_id: Optional[int] = 2
    title: str
    content: str
    location: Optional[str] = "Palestine, Gaza"
    ai_validated: Optional[bool] = False
    vote_count: Optional[int] = 0

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    location: Optional[str]

class PostOut(PostBase):
    id: int

    class Config:
        orm_mode = True   # Correct for FastAPI 0.95+ and SQLAlchemy ORM
