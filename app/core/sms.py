def send_sms(phone: str, message:str):
    print(f"Sending SMS to {phone}: {message}")
    # Here you would integrate with an SMS gateway API to send the message
    # For example, using Twilio or another service
    # twilio_client.messages.create(to=phone, from_="YourTwilioNumber", body=message)   