from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.exercise import TerminalExerciseCreate, TerminalExerciseResponse
from app.models.exercise import TerminalExercise

router = APIRouter()

@router.get("/", response_model=List[TerminalExerciseResponse])
def get_exercises(db: Session = Depends(get_db)):
    """Retrieve a list of terminal exercises."""
    exercises = db.query(TerminalExercise).all()
    return exercises

@router.post("/", response_model=TerminalExerciseResponse)
def create_exercise(exercise: TerminalExerciseCreate, db: Session = Depends(get_db)):
    """Create a new terminal exercise."""
    db_exercise = TerminalExercise(**exercise.dict())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

@router.get("/{exercise_id}", response_model=TerminalExerciseResponse)
def get_exercise(exercise_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific terminal exercise by ID."""
    exercise = db.query(TerminalExercise).filter(TerminalExercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise
