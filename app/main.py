from fastapi import FastAPI, Request
from sqlmodel import SQLModel
from app.db.session import engine
from app.api import register, jobs, respond, dashboard, feedback
from pydantic import BaseModel

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(register.router)
app.include_router(jobs.router)
app.include_router(respond.router)
app.include_router(dashboard.router)
app.include_router(feedback.router)


@app.post("/sms-webhook")
async def receive_sms(request: Request):
    # Twilio sends form data, not JSON
    form_data = await request.form()
    
    # Extract the important information from the request
    from_number = form_data.get("From")
    message_body = form_data.get("Body")
    
    # Print the received data for your research
    print("--- New Incoming SMS ---")
    print(f"From: {from_number}")
    print(f"Message: {message_body}")
    print("------------------------")
    
    # Here, you would implement your research logic.
    # For example, you could save the message to a database,
    # analyze the sentiment, or send an automated reply.
    
    # You can also send a reply back to the user from here
    # (using the Twilio API client as shown in step 1).
    
    return {"status": "ok"}