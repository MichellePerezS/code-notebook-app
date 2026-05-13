from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.lesson import BoardLessonCreate, BoardLessonResponse

router = APIRouter()

# Stubs for now
@router.get("/", response_model=List[BoardLessonResponse])
def get_lessons():
    """Retrieve a list of board lessons."""
    return []

@router.post("/", response_model=BoardLessonResponse)
def create_lesson(lesson: BoardLessonCreate):
    """Create a new board lesson."""
    # Stub response
    return {"id": 1, **lesson.dict()}

@router.get("/{lesson_id}", response_model=BoardLessonResponse)
def get_lesson(lesson_id: int):
    """Retrieve a specific board lesson by ID."""
    raise HTTPException(status_code=404, detail="Lesson not found")
