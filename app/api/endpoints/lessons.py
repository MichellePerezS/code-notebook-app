from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.lesson import BoardLessonCreate, BoardLessonResponse
from app.models.lesson import BoardLesson

router = APIRouter()

@router.get("/", response_model=List[BoardLessonResponse])
def get_lessons(db: Session = Depends(get_db)):
    """Retrieve a list of board lessons."""
    lessons = db.query(BoardLesson).all()
    return lessons

@router.post("/", response_model=BoardLessonResponse)
def create_lesson(lesson: BoardLessonCreate, db: Session = Depends(get_db)):
    """Create a new board lesson."""
    db_lesson = BoardLesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

@router.get("/{lesson_id}", response_model=BoardLessonResponse)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific board lesson by ID."""
    lesson = db.query(BoardLesson).filter(BoardLesson.id == lesson_id).first()
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson
