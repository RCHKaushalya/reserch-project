from sqlmodel import Field, SQLModel
from typing import Optional

class Feedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int
    worker_id: int
    rating: int
    comment: Optional[str]