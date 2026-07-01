from pydantic import BaseModel


class JobSchema(BaseModel):
    title: str
    company: str
    role: str
    location: str
    tags: str
    description: str
    url: str
    date: str

    class Config:
        from_attributes = True