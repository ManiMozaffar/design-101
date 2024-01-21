import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import firebase_admin
from firebase_admin import storage


def is_valid_email(email: str) -> bool:
    """
    Validate the email address using a regular expression.
    """
    pattern = r"/^[a-zA-Z0-9. _-]+@[a-zA-Z0-9. -]+\. [a-zA-Z]{2,4}$/"
    return re.match(pattern, email) is not None


def initialize_app(cred):
    return firebase_admin.initialize_app(cred)


def get_bucket_path(bucket_name: str) -> str:
    bucket = storage.bucket(bucket_name)
    return bucket.path


def send_email(
    recipient_address: str,
    sender_address: str,
    title: str,
    content: str,
    smtp_addr: str,
):
    if not is_valid_email(recipient_address) or not is_valid_email(sender_address):
        raise ValueError("Invalid email address.")

    # Create the container email message.
    msg = MIMEMultipart()
    msg["Subject"] = title
    msg["From"] = sender_address
    msg["To"] = recipient_address
    msg.attach(MIMEText(content, "plain"))
    with smtplib.SMTP(smtp_addr, 587) as server:
        server.starttls()
        server.login(sender_address, "password")
        server.send_message(msg)

    print("Email sent successfully.")


if __name__ == "__main__":
    send_email(
        "recipient@example",
        "sender@example",
        "Hey",
        "Welcome to GitOverHere contents",
        "smtp_addr",
    )
