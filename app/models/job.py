from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    location: str
    budget: Optional[str]
    posted_by: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
