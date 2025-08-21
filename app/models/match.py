from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class Match(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int
    worker_id: int
    response: Optional[str] = None
    responded_at: Optional[datetime]
    confirmed: bool = False