from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class BoardLesson(Base):
    __tablename__ = "board_lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    theory_content = Column(Text, nullable=False)
    syntax_tips = Column(Text, nullable=True)
    diagram_url = Column(String, nullable=True)
    language = Column(String, nullable=False) # e.g. "Python" or "C++"
