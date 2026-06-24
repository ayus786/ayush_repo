class EmailSender:
    def send_email(self, subject, recipient):
        print(f"Sending email to {recipient}: {subject}")

# This user class violates SRP: it does more than one thing: encapsulate user data AND register user
class User:
    def __init__(self, username, email):
        self.username = username  # Public attributes
        self.email = email

    def register(self):
        """Register the user and send a welcome email."""
        # Register user logic (could be saving to a database, etc.)
        print(f"Registering user: {self.username}")

        # Send email notification
        email_sender = EmailSender()
        email_sender.send_email("Welcome to our platform!", self.email)

# Example usage
user = User(username="john_doe", email="john.doe@example.com")
user.register()
