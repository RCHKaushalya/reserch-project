from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.otp import generate_otp

router = APIRouter()

@router.post("/register")
def register_user(data: UserCreate, session: Session = Depends(get_session)):
    user = User(**data.dict())

    session.add(user)
    session.commit()
    session.refresh(user)

    otp = generate_otp()

    return {"user_id": user.id, "otp": otp}