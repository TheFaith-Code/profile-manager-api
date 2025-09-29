from pydantic import BaseModel, EmailStr
from typing import Optional

class Profile(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = None
    bio: Optional[str] = None

class ProfileCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    bio: Optional[str] = None

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    bio: Optional[str] = None
