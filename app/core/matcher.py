from app.models.user import User
from app.models.job import Job
from sqlmodel import Session, select

def find_matching_worker(job: Job, session: Session):
    query = select(User).where(
        User.skills.contains(job.category),
        User.district == job.location
    )

    return session.exec(query).all()

