from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    user_id: int
    category_id: int
    subcategory_id: Optional[int]
    title: str
    content: str
    location: Optional[str]
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
        from_attributes = True
