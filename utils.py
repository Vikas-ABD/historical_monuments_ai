import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# SMTP CONFIGURATION
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = os.getenv('EMAIL_USERNAME')
PASSWORD = os.getenv('EMAIL_PASSWORD')

# Function to send email
def send_email(receiver_email: str, subject: str, body: str) -> bool:
    """
    Sends an email with the given subject and body.
    Connects and disconnects the SMTP server per email to avoid stale connections.
    """
    try:
        # Establish a fresh SMTP connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            print("✅ SMTP connection initialized.")

            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = USERNAME
            msg['To'] = receiver_email
            msg.set_content(body)

            server.send_message(msg)
            print(f"✅ Email sent to {receiver_email}")
            return True

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

