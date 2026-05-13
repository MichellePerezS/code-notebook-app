from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(
    title="Code Notebook API",
    description="Backend for the hybrid analog-digital programming education platform.",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the Code Notebook API!"}
