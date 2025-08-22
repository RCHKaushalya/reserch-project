# Import the Twilio client
from twilio.rest import Client
import os

# DONT store these directly in your code. Use environment variables.
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

# The message to send
message_body = "Hello from my research project! Please reply to this message to participate."

# Your Twilio number and the recipient's number
from_number = "+12513026214"  # Your Twilio phone number
to_number = "+94788761681"    # The user's Sri Lankan number

message = client.messages.create(
    to=to_number,
    from_=from_number,
    body=message_body
)

print(f"Message sent successfully! SID: {message.sid}")