from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.session import engine
from app.api import register, jobs, respond, dashboard, feedback

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(register.router)
app.include_router(jobs.router)
app.include_router(respond.router)
app.include_router(dashboard.router)
app.include_router(feedback.router)