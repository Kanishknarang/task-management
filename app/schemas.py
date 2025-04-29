from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
