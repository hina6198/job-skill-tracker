from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    role = Column(String)
    location = Column(String)
    tags = Column(Text)
    description = Column(Text)
    url = Column(String)
    date = Column(String)