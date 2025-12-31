from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# User registration input
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

# User output (what we return after registration/login)
class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True  # Pydantic v2

# Login input
class Login(BaseModel):
    email: EmailStr
    password: str

# Token output (JWT)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Task input/output
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    owner_id: int

    class Config:
        from_attributes = True