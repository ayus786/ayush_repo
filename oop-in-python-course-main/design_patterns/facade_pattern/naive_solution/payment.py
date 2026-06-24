class Payment:
    def __init__(self, name: str, card_number: str, amount: float):
        self._name = name
        self._card_number = card_number
        self._amount = amount

    def pay(self):
        print(f"Charging card with name {self._name}")
