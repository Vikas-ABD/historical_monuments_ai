from langchain.tools import tool
import time
from Tools.send_otp_tool import otp_store  # Access the OTP store from send_otp_tool

@tool
def validate_otp_email(receiver_email: str, user_otp: str) -> str:
    """ 
    Validates the OTP that the user received in their email.
    Use this tool to verify whether the user has entered the correct OTP before confirming their email verification.
    """
    if receiver_email not in otp_store:
        return "❌ No OTP was sent to this email address. Please request a new one."

    otp_entry = otp_store.get(receiver_email)

    # Check for expiration
    if time.time() > otp_entry['expires_at']:
        del otp_store[receiver_email]
        return "❌ The OTP has expired. Please request a new one."

    # Check if OTP matches
    if otp_entry['otp'] != user_otp:
        return "❌ The OTP is incorrect. Please check and try again."

    del otp_store[receiver_email]
    return "✅ OTP validated successfully! Your email is now verified."

