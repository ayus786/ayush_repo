from design_patterns.facade_pattern.naive_solution.authenticator import Authenticator
from design_patterns.facade_pattern.naive_solution.inventory import Inventory
from design_patterns.facade_pattern.naive_solution.payment import Payment
from design_patterns.facade_pattern.naive_solution.order_fulfillment import (
    OrderFulfillment,
)


class OrderService:
    def create_order(self, order_req):
        auth = Authenticator()
        auth.authenticate()

        inventory = Inventory()
        for item_id in order_req.item_ids:
            inventory.check_inventory(item_id)

        payment = Payment(order_req.name, order_req.card_number, order_req.amount)
        payment.pay()

        order_fulfillment = OrderFulfillment(inventory)
        order_fulfillment.fulfill(order_req.name, order_req.address, order_req.item_ids)

    # We could also add other order service methods, like `cancel_order()` and `update_order()`...
