from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
        from_attributes = True

class HabitTrackingCreate(BaseModel):
    user_id: int
    date: date
    lessons_completed: int = 0
    exercises_completed: int = 0
    current_streak: int = 0

class HabitTrackingResponse(HabitTrackingCreate):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
