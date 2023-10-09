class Notification:
    def __init__(self, content, recipient, notification_type):
        self.content = content
        self.recipient = recipient
        self.notification_type = notification_type

    def send(self):
        if self.notification_type == "SMS":
            print(f"Sending SMS to {self.recipient}: {self.content}")
        elif self.notification_type == "Email":
            print(f"Sending Email to {self.recipient}: {self.content}")
        else:
            print("Invalid notification type!")
        # Now it's 3 lines... what if they grow big? would you dare to maintain it?!
        # This OF COURSE makes more sense in low code base, like most design patterns
        # But remember, once your code grows big, you need to decouple it.
        # And creator pattern is just a way of doing that.


sms_notification = Notification("Hello!", "123-456-7890", "SMS")
sms_notification.send()

email_notification = Notification("Hello!", "example@example.com", "Email")
email_notification.send()
