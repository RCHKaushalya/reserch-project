from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from datetime import datetime
from app.db.session import get_session
from app.models.match import Match

router = APIRouter()

@router.post("/respond-job")
def respond_job(job_id: int, worker_id: int, response: str, session: Session = Depends(get_session)):
    match = session.exec(
        select(Match).where(Match.job_id == job_id, Match.worker_id == worker_id)
    ).first()

    if match:
        match.response = "interested" if response == "1" else "not_interested"
        match.responded_at = datetime.utcnow()
        session.add(match)
        session.commit()
        return {"status": "Response recorded"}
    
    return {"error": "Match not found"}
