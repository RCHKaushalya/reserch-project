from sqlmodel import SQLModel, Field
from typing import Optional

class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    required_skills: str
    location: str
    employer_name: str
    contact: str