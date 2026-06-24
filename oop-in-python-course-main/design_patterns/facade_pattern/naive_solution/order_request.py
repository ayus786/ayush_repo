# User-submitted order request data
class OrderRequest:
    def __init__(self):
        self.name = "danny"
        self.card_number = "1234"
        self.amount = 20.99
        self.address = "123 Springfield Way, Texas"
        # item IDs user wants to order
        self.item_ids = ["123", "423", "555", "989"]
