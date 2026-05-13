from pydantic import BaseModel
from typing import Optional

class TerminalExerciseCreate(BaseModel):
    lesson_id: int
    title: str
    problem_statement: str
    initial_code: Optional[str] = None
    expected_output: str
    difficulty: str

class TerminalExerciseResponse(TerminalExerciseCreate):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
