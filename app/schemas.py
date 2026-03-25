from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponde(BaseModel):
    id: int
    name: str
    email: str

class Config:
    from_attributes = True

class TokenResponse(BaseModel):
    token: str

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: str
    description: Optional[str]

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None 
    completed: Optional[bool] = None 

class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None 
    completed: bool 
    owner_id: int 

    class Config:
        from_attributes = True

class TodoListResponse(BaseModel):
    data: list[TodoResponse]
    page: int 
    limit: int 
    total: int 