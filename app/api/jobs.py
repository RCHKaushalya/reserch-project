from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.models.job import Job
from app.schemas.job import JobCreate
from app.core.matcher import find_matching_worker
from app.core.sms import send_sms
from app.models.match import Match

router = APIRouter()

@router.post("/post-job")
def post_job(data: JobCreate, session: Session = Depends(get_session)):
    job = Job(**data.dict())

    session.add(job)
    session.commit()
    session.refresh(job)

    workers = find_matching_worker(job, session)
    for worker in workers:
        msg = f"New job posted: {job.title} in {job.location}. Reply 1 to accept."
        send_sms(worker.phone, msg)
        match = Match(job_id=job.id, worker_id=worker.id)
        session.add(match)
    
    session.commit()

    return {"job_id": job.id, "notified": len(workers)}