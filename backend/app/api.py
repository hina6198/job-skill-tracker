from fastapi import APIRouter
from sqlalchemy.orm import Session
import pandas as pd

from .database import SessionLocal
from .models import Job

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to Job Skill Tracker API"
    }


@router.get("/health")
def health():
    return {
        "status": "API Running Successfully"
    }


@router.get("/jobs")
def get_jobs(role: str = None):
    db: Session = SessionLocal()

    query = db.query(Job)

    if role:
        query = query.filter(Job.role.ilike(f"%{role}%"))

    jobs = query.all()

    db.close()

    return jobs


@router.get("/skills")
def get_skills():
    df = pd.read_csv("data/skill_frequency.csv")
    return df.to_dict(orient="records")


@router.get("/roles")
def get_roles():
    db: Session = SessionLocal()

    roles = db.query(Job.role).distinct().all()

    db.close()

    return [role[0] for role in roles if role[0]]