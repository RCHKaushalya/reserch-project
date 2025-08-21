from sqlmodel import Session, select
from app.models.feedback import Feedback

def calculate_worker_score(worker_id: int, session: Session):
    feedbacks = session.exec(
        select(Feedback).where(Feedback.worker_id == worker_id)
    ).all()

    if not feedbacks:
        return 0
    
    avg_rating = sum(f.rating for f in feedbacks) / len(feedbacks)
    return round(avg_rating, 2)