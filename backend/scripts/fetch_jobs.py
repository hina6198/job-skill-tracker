import json
from pathlib import Path

import requests

from app.database import SessionLocal, engine, Base
from app.models import Job

Base.metadata.create_all(bind=engine)

URL = "https://remoteok.com/api"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

response.raise_for_status()

jobs = response.json()

Path("data").mkdir(exist_ok=True)

with open("data/raw_jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=2)

db = SessionLocal()

db.query(Job).delete()

for job in jobs:

    if not isinstance(job, dict):
        continue

    db_job = Job(
        title=job.get("position", ""),
        company=job.get("company", ""),
        role=job.get("position", ""),
        location=job.get("location", ""),
        tags=", ".join(job.get("tags", [])),
        description=job.get("description", ""),
        url=job.get("url", ""),
        date=str(job.get("date", ""))
    )

    db.add(db_job)

db.commit()

db.close()

print("Jobs saved successfully!")