from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Tool(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    owner_mobile: str
    location: str
    available: bool = True

class LendingRequest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tool_id: int
    borrower_mobile: str
    request_date: datetime = Field(default_factory=datetime.utcnow)
    status: str = 'pending' # pending, approved, rejected