from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, TIMESTAMP, func
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    subcategory_id = Column(Integer, nullable=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    location = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    ai_validated = Column(Boolean, default=False)
    vote_count = Column(Integer, default=0)
