from fastapi import APIRouter
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import Job

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "API Running Successfully"}


@router.get("/jobs")
def get_jobs():
    db: Session = SessionLocal()

    jobs = db.query(Job).limit(20).all()

    db.close()

    return jobs