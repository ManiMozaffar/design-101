import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailString(str):
    def __new__(cls, value):
        pattern = r"/^[a-zA-Z0-9. _-]+@[a-zA-Z0-9. -]+\. [a-zA-Z]{2,4}$/"
        if re.match(pattern, value) is not None:
            raise ValueError("Invalid email address")
        return str.__new__(cls, value)


class EmailMIMEMultipart:
    def __init__(self, title: str, _from: EmailString, to: EmailString, content: str):
        if len(content) == 0:
            raise ValueError("Invalid content or subject")

        if len(title) == 0:
            raise ValueError("Invalid content or subject")

        self.msg = MIMEMultipart()
        self.to_addrs = to
        self.msg["Subject"] = title
        self.msg["From"] = _from
        self.msg["To"] = to
        self.msg.attach(MIMEText(content, "plain"))


class MailClient:
    def __init__(self, sender_address: EmailString, smtp_addr: str, password: str):
        self.smtp = smtplib.SMTP(smtp_addr, 587)
        with self.smtp as server:
            server.starttls()
            server.login(sender_address, password)
        self.sender_address = sender_address

    def send_emails(self, messages: list[EmailMIMEMultipart]):
        with self.smtp as server:
            for body in messages:
                server.send_message(
                    body.msg,
                    from_addr=self.sender_address,
                    to_addrs=body.to_addrs,
                )

    def build_email_body(self, title: str, content: str, rec_addr: EmailString):
        return EmailMIMEMultipart(title, self.sender_address, rec_addr, content)


def main():
    sender_address = EmailString("test@example.com")
    smtp_addr = "127.0.0.1"
    password = "Test12345"
    client = MailClient(sender_address, smtp_addr, password)
    emails = [
        client.build_email_body(
            "title",
            "content",
            EmailString("rec1@example.com"),
        ),
        client.build_email_body(
            "title",
            "content",
            EmailString("rec2@example.com"),
        ),
        client.build_email_body(
            "title",
            "content",
            EmailString("rec3@example.com"),
        ),
    ]
    client.send_emails(emails)


if __name__ == "__main__":
    main()
