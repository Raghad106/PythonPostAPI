from sqlalchemy.orm import Session
import models
import schemas


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session):
    return db.query(models.Post).all()

def update_post(db: Session, post_id: int, post_data: schemas.PostUpdate):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post:
        for key, value in post_data.dict(exclude_unset=True).items():
            setattr(post, key, value)
        db.commit()
        db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post
