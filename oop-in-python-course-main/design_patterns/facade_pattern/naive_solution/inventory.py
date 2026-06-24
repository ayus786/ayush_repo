class Inventory:
    def check_inventory(self, item_id: str) -> bool:
        return True  # just return true to keep the example simple

    def reduce_inventory(self, item_id: str, amount: int):
        # In real app this would reduce the amount in a database
        print(f"Reducing inventory of {item_id} by {amount}")
