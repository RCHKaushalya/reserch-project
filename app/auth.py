import random
from typing import Dict

# Temporary in-memory store for OTPs
otp_store: Dict[str, str] = {}

def generate_otp(mobile: str) -> str:
    """Generate a random 6-digit OTP."""
    otp = str(random.randint(100000, 999999))
    otp_store[mobile] = otp
    return otp

def verify_otp(mobile: str, otp: str) -> bool:
    """Verify the OTP for a given mobile number."""
    return otp_store.get(mobile) == otp