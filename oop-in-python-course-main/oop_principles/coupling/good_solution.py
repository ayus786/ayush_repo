from abc import ABC, abstractmethod

# Interface for notifications so all notification services provide consistent api for clients (polymorphism and dependency injection = FLEXIBLE!)
class NotificationService(ABC):
    """Interface-like base class for notification services."""

    @abstractmethod
    def send_notification(self, message: str):
        """Abstract method to send a notification."""
        pass

# Concrete implementation
class EmailService(NotificationService):
    def send_notification(self, message: str):
        print(f"Sending email: {message}")

# Concrete implementation
class MobileService(NotificationService):
    def send_notification(self, message: str):
        print(f"Sending text message: {message}")

# In this class, we introduce dependency injection and Python's type hinting to the student.
class Order:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def create(self):
        # Perform order creation logic, e.g. validate order details, check product stock, save to database...

        self.notification_service.send_notification(
            "Hi, your order was placed successfully and will be with you within 2-5 working days"
        )

order = Order(EmailService())
order.create()

order2 = Order(MobileService())
order2.create()
