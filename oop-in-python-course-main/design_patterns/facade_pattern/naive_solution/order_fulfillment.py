from design_patterns.facade_pattern.naive_solution.inventory import Inventory


class OrderFulfillment:
    def __init__(self, inventory: Inventory):
        # protected attribute to hold the inventory instance
        self._inventory = inventory

    def fulfill(self, name: str, address: str, items: list[str]):
        print("Inserting order into database")
        for item in items:
            self._inventory.reduce_inventory(item, 1)
