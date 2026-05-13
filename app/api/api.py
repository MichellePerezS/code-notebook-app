from fastapi import APIRouter
from app.api.endpoints import lessons, exercises, users

api_router = APIRouter()
api_router.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
api_router.include_router(exercises.router, prefix="/exercises", tags=["exercises"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
