import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# SMTP CONFIGURATION (fetched securely from environment)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = os.getenv('EMAIL_USERNAME')
PASSWORD = os.getenv('EMAIL_PASSWORD')

# Initialize SMTP connection ONCE
def init_smtp():
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(USERNAME, PASSWORD)
        print("✅ SMTP connection initialized.")
        return server
    except Exception as e:
        print(f"❌ SMTP initialization failed: {e}")
        return None

# Initialize globally
smtp_server = init_smtp()

# Function to send email
def send_email(receiver_email: str, subject: str, body: str) -> bool:
    """
    Sends an email with the given subject and body.
    """
    if smtp_server is None:
        print("❌ SMTP server not initialized.")
        return False

    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = USERNAME
        msg['To'] = receiver_email
        msg.set_content(body)

        smtp_server.send_message(msg)
        print(f"✅ Email sent to {receiver_email}")
        return True

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

# Optional: Close SMTP connection
def close_smtp():
    if smtp_server:
        smtp_server.quit()
        print("✅ SMTP connection closed.")
