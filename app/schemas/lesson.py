from pydantic import BaseModel
from typing import Optional

class BoardLessonCreate(BaseModel):
    title: str
    theory_content: str
    syntax_tips: Optional[str] = None
    diagram_url: Optional[str] = None
    language: str

class BoardLessonResponse(BoardLessonCreate):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
