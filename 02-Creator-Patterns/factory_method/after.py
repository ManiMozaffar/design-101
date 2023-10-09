from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self):
        pass


class SMS(Notification):
    def __init__(self, content, phone_number):
        self.content = content
        self.phone_number = phone_number

    def send(self):
        print(f"Sending SMS to {self.phone_number}: {self.content}")


class Email(Notification):
    def __init__(self, content, email_address):
        self.content = content
        self.email_address = email_address

    def send(self):
        print(f"Sending Email to {self.email_address}: {self.content}")


class NotificationFactory(ABC):
    def notify(self, content, recipient):
        notification = self.create_notification(content, recipient)
        notification.send()

    @abstractmethod
    def create_notification(self, content, recipient) -> Notification:
        pass


class SMSNotificationFactory(NotificationFactory):
    def create_notification(self, content, recipient):
        return SMS(content, recipient)


class EmailNotificationFactory(NotificationFactory):
    def create_notification(self, content, recipient):
        return Email(content, recipient)


factory = SMSNotificationFactory()
factory.notify("Hello!", "123-456-7890")
