from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.models.feedback import Feedback

router = APIRouter()

@router.post("/submit-feedback")
def submit_feedback(data: Feedback, session: Session = Depends(get_session)):
    session.add(data)
    session.commit()

    return {"status": "Feedback recorded"}