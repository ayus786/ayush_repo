# Here, each class is responsible for just one thing, and only has one reason to change.

class EmailSender:
    def send_email(self, subject, recipient):
        print(f"Sending email to {recipient}: {subject}")

class User:
    def __init__(self, username, email):
        self.username = username  # Public attributes
        self.email = email

class UserService:
    # Note: see README for guidance on whether to pass `user` to each service method, or to use composition
    def register(self, user):
        """Register the user and send a welcome email."""
        # Register user logic (could be saving to a database, etc.)
        print(f"Registering user: {user.username}")

        # Send email notification
        email_sender = EmailSender()
        email_sender.send_email("Welcome to our platform!", user.email)

# Example usage
user = User(username="john_doe", email="john.doe@example.com")
user_service = UserService()
user_service.register(user)
