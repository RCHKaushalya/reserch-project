from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    nic: str
    district: str
    phone: str
    skill: str
    is_sms_user: bool = False