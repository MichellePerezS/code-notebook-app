from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.exercise import TerminalExerciseCreate, TerminalExerciseResponse

router = APIRouter()

@router.get("/", response_model=List[TerminalExerciseResponse])
def get_exercises():
    """Retrieve a list of terminal exercises."""
    return []

@router.post("/", response_model=TerminalExerciseResponse)
def create_exercise(exercise: TerminalExerciseCreate):
    """Create a new terminal exercise."""
    return {"id": 1, **exercise.dict()}

@router.get("/{exercise_id}", response_model=TerminalExerciseResponse)
def get_exercise(exercise_id: int):
    """Retrieve a specific terminal exercise by ID."""
    raise HTTPException(status_code=404, detail="Exercise not found")
