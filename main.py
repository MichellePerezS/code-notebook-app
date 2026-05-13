from fastapi import FastAPI
from app.api.api import api_router
from app.db.base import Base
from app.db.session import engine

# Import all models here to ensure they are registered with Base before creating tables
from app.models.lesson import BoardLesson
from app.models.exercise import TerminalExercise
from app.models.user import User, HabitTracking

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Code Notebook API",
    description="Backend for the hybrid analog-digital programming education platform.",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the Code Notebook API!"}
