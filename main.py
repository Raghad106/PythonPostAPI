from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from post import database, models, schemas, crud
from post.database import Base


models.Base.metadata.create_all(bind=database.engine)
app = FastAPI(title="FastAPI + PostgreSQL API")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts/", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

@app.get("/posts/", response_model=list[schemas.PostOut])
def read_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)

@app.put("/posts/{post_id}", response_model=schemas.PostOut)
def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    updated = crud.update_post(db, post_id, post)
    if not updated:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_post(db, post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Deleted successfully"}
