def send_sms(phone: str, message:str):
    print(f"Sending SMS to {phone}: {message}")
    # Here you would integrate with an SMS gateway API to send the message
    # For example, using Twilio or another service
    # twilio_client.messages.create(to=phone, from_="YourTwilioNumber", body=message)   

def send_confirmation_sms(phone: str, job_category: str, location: str):
    message =  f'You have been selected for a {job_category} job in {location}. Please prepare'
    send_sms(phone, message)