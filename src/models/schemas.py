from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False
    class Config:
        orm_mode = True

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None
