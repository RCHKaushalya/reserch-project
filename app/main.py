from fastapi import FastAPI, HTTPException
from sqlmodel import Session
from app.database import create_db_and_tables, engine
from app.models import User
from app.auth import generate_otp, verify_otp

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to the System"}

@app.post("/register")
def register_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

@app.post("/request-otp")
def request_otp(mobile: str):
    otp = generate_otp(mobile)
    return {"mobile": mobile, "otp": otp}

@app.post("/verify-otp")
def verify_user_otp(mobile: str, otp: str):
    if verify_otp(mobile, otp):
        return {"status": "verified"}
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP")
