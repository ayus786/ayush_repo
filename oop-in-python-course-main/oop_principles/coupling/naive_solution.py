# Coupling

class EmailSender:
    def send(self, message):
        print(f"Sending email: {message}")

class Order:
    def create(self):
        # Perform order creation logic, e.g. validate order details, check product stock, save to database...

        # Send email notification
        email = EmailSender()
        email.send(
            "Hi, your order was placed successfully and will be with you within 2-5 working days"
        )

order = Order()
order.create()

# LOGS:
# Sending email to danny@gmail.com: Hi Danny, your order was placed successfully and will be with you within 2-5 working days

# PROBLEM: Order class is tightly coupled to EmailSender. What if in future we need to send text message? We have to modify this code, violating open/closed.
