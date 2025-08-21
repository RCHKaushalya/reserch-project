from pydantic import BaseModel

class JobCreate(BaseModel):
    category: str
    location: str
    budget: str
    posted_by: int