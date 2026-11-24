class Notification:
    def send(self):
        print("Sending a generic notification.")


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email.")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS.")


# Create objects
n1 = Notification()
n2 = EmailNotification()
n3 = SMSNotification()
n4 = EmailNotification()
n5 = SMSNotification()

# Store objects in a list
notifications = [n1, n2, n3, n4, n5]

# Send all notifications using a single loop
for notification in notifications:
    notification.send()