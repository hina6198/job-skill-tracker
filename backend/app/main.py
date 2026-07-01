from fastapi import FastAPI

from .database import Base, engine
from .api import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Skill Tracker API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Job Skill Tracker API"
    }