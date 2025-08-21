from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.match import Match
from app.models.user import User
from app.core.sms import send_confirmation_sms

router = APIRouter()

@router.get("/job-responses/{job_id}")
def get_job_responses(job_id: int, session: Session = Depends(get_session)):
    matches = session.exec(
        select(Match).where(Match.job_id == job_id, Match.response == "interested")
    ).all()

    result = []

    for m in matches:
        worker = session.get(User, m.worker_id)
        result.append({
            "worker_id": worker.id,
            "name": worker.name,
            "skills": worker.skills,
            "district": worker.district,
            "responded_at": m.responded_at
        })
    
    return result

@router.post("/confirm-worker")
def confirm_worker(job_id: int, worker_id: int, session: Session = Depends(get_session)):
    match = session.exec(
        select(Match).where(Match.job_id == job_id, Match.worker_id == worker_id)
    ).first()

    worker = session.get(User, worker_id)

    if match:
        match.confirmed = True
        Session.add(match)
        session.commit()
        send_confirmation_sms(worker.phone, match.job.category, match.job.location)
        return {"status": "Worker confirmed"}
    return {"error": "Match not found"}