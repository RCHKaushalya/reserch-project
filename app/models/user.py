from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    nic: str
    district: str
    phone: str
    skill: str
    is_sms_user: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

