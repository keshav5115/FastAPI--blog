from fastapi import FastAPI,Depends,status
from sqlalchemy.orm import Session 
import uvicorn
from typing import List
from . import models,schema
from .database import engine,SessionLocal
app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal(bind=engine)
    try:
        yield db
    finally:
        db.close()

@app.post("/bloger",status_code=201)
def create_blog(request: schema.Blog,db:Session=Depends(get_db)):
    db_blog = models.Blog(**request.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog



@app.get("/bloger{id}",response_model=schema.BlogShow )
def read_blog(id:int,db:Session=Depends(get_db)):
    return db.query(models.Blog).filter(models.Blog.id ==id).first()

@app.put("/bloger/{id}")
def update_blog(id: int, request: schema.Blog, db: Session=Depends(get_db)):

    db_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if db_blog:
        db_blog.title = request.title
        db.commit()
        db.refresh(db_blog)
        return db_blog
    else:
        return {"message": "Blog not found"}

@app.delete("/bloger/{id}")
def delete_blog(id: int, db: Session=Depends(get_db)):
    db_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if db_blog:
        db.delete(db_blog)
        db.commit()
        return {"message": "Blog deleted"}
    else:
        return {"message": "Blog not found"}
    # return {"message": "Delete blog with ID: " + str(id)}

@app.get("/bloger",response_model=List[schema.BlogShow])
def all_blog(db: Session=Depends(get_db)):
    return db.query(models.Blog).all()




# @app.post("/user")
# def create_user(db: Session=Depends(get_db):





# if __name__ == '__main__':
#     uvicorn.run(app, host='localhost', port=8000)