from fastapi import FastAPI, HTTPException
from sqlmodel import Session
from app.database import create_db_and_tables, engine
from app.models import User
from app.auth import generate_otp, verify_otp, mark_verified, is_verified
from app.job_routes import router as job_router
from app.tool_routes import router as tool_router

app = FastAPI()
app.include_router(job_router)
app.include_router(tool_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to the System"}

@app.post("/register")
def register_user(user: User):
    if not is_verified(user.mobile):
        raise HTTPException(status_code=403, detail="Mobile number not verified")

    with Session(engine) as session:
        exisiting = session.query(User).filter(User.mobile == user.mobile).first()
        if exisiting:
            raise HTTPException(status_code=409, detail="User already exists")
        
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
        mark_verified(mobile)
        return {"status": "verified"}
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP")

@app.get("/profile/{mobile}")
def get_user_profile(mobile: str):
    with Session(engine) as session:
        user = session.query(User).filter(User.mobile == mobile).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

@app.put("/profile/{mobile}")
def update_user_profile(mobile: str, update_data: User):
    with Session(engine) as session:
        user = session.query(User).filter(User.mobile == mobile).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user.name = update_data.name or user.name
        user.lacation = update_data.lacation or user.lacation
        user.skills = update_data.skills or user.skills

        session.commit()
        session.refresh(user)
        return user