from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.session import engine
from app.api import register, jobs

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(register.router)
app.include_router(jobs.router)