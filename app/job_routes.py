from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.database import engine
from app.job_models import Job
from app.models import User

router = APIRouter()

@router.post('/jobs')
def post_job(job: Job):
    with Session(engine) as session:
        session.add(job)
        session.commit()
        session.refresh(job)
        return job

@router.get('/jobs/{mobile}')
def get_matching_jobs(mobile: str):
    with Session(engine) as session:
        user = session.query(User).filter(User.mobile == mobile).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user_skills = set(skill.strip().lower() for skill in user.skills.split(','))
        jobs = session.exec(select(Job)).all()

        matched_jobs = []

        for job in jobs:
            job_skills = set(skill.strip().lower() for skill in job.required_skills.split(','))
            if user_skills & job_skills and user.lacation.lower() in job.location.lower():
                matched_jobs.append(job)
        
        return matched_jobs