from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user import UserCreate, UserResponse, HabitTrackingCreate, HabitTrackingResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    """Register a new user."""
    return {"id": 1, "is_active": True, "email": user.email, "username": user.username}

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """Retrieve a user's details."""
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/{user_id}/habits", response_model=List[HabitTrackingResponse])
def get_user_habits(user_id: int):
    """Retrieve habit tracking for a user."""
    return []

@router.post("/{user_id}/habits", response_model=HabitTrackingResponse)
def log_habit(user_id: int, habit: HabitTrackingCreate):
    """Log daily habit tracking for a user."""
    if user_id != habit.user_id:
        raise HTTPException(status_code=400, detail="User ID mismatch")
    return {"id": 1, **habit.dict()}
