from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from datetime import date
import uvicorn

app = FastAPI()

@app.get('/')
def sample():
    return {"message": "This is a sample API endpoint"}



@app.get('/sample/unpublished')
def unpublished():
    return {"message": "This API endpoint provides unpublished sample applications"}


@app.get('/blog')
def index(limit=10,published:bool=False,sort:Optional['str']=None):
    if published:
        return {"message": f"{limit} records only{published}"}
    else:
        return {"message": "All records"}
#http://localhost:8000/blog?limit=10
#http://localhost:8000/blog?limit=10&published=false

@app.get('/sample/{id}')
def about(id:int):
    return {"message": f"This API endpoint provides information about the sample application{id}"}

@app.get('/sample/{id}/comment')
def comment(id:int,limit=10,published:bool=False):
    return {"message": f"This API endpoint provides comments for the sample application{id}"}

class User(BaseModel):
    id: int
    name: str
    joined: date
    Published: bool


@app.post('/sample/user')
def create_user(user: User):
    return {"message": f"User {user.name} has been created"}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
