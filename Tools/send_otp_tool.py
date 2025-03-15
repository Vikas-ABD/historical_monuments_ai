from langchain.tools import tool
import random
import string
import time
from utils import send_email

# Temporary OTP store
otp_store = {}

@tool
def send_otp_email(receiver_email: str) -> str:
    """
    Sends a 6-digit OTP to the specified email address so the user can verify their identity.
    Use this tool after the user provides an email address to confirm their contact before sharing more details.
    """
    otp = ''.join(random.choices(string.digits, k=6))
    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}. It is valid for 5 minutes."

    success = send_email(receiver_email, subject, body)

    if success:
        otp_store[receiver_email] = {'otp': otp, 'expires_at': time.time() + 300}
        return f"✅ OTP has been sent to {receiver_email}. Please check your inbox."
    else:
        return f"❌ Unable to send OTP to {receiver_email}. Please try again later."

