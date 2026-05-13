from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.base import Base

class TerminalExercise(Base):
    __tablename__ = "terminal_exercises"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("board_lessons.id"), nullable=False)
    title = Column(String, index=True, nullable=False)
    problem_statement = Column(Text, nullable=False)
    initial_code = Column(Text, nullable=True)
    expected_output = Column(Text, nullable=False)
    difficulty = Column(String, nullable=False) # e.g. "Easy", "Medium", "Hard"
