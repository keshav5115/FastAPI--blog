from pydantic import BaseModel


class Blog(BaseModel):
    id:int
    title: str


class BlogShow(BaseModel):
    title: str
    class config():
        orm_mode = True



class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_active: bool
