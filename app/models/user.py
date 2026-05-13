from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    habits = relationship("HabitTracking", back_populates="user")

class HabitTracking(Base):
    __tablename__ = "habit_tracking"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False, index=True)
    lessons_completed = Column(Integer, default=0)
    exercises_completed = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)

    user = relationship("User", back_populates="habits")
