# This file shows all of the steps that every client would have to do to create an order.
# Run this on the terminal: `python -m design_patterns.facade_pattern.naive_solution.main`

from design_patterns.facade_pattern.naive_solution.order_request import OrderRequest
from design_patterns.facade_pattern.naive_solution.authenticator import Authenticator
from design_patterns.facade_pattern.naive_solution.inventory import Inventory
from design_patterns.facade_pattern.naive_solution.payment import Payment
from design_patterns.facade_pattern.naive_solution.order_fulfillment import (
    OrderFulfillment,
)

# Order request contains info that user has submitted when requesting to make an order
order_req = OrderRequest()

auth = Authenticator()
auth.authenticate()

inventory = Inventory()
for item_id in order_req.item_ids:
    inventory.check_inventory(item_id)

payment = Payment(order_req.name, order_req.card_number, order_req.amount)
payment.pay()

order_fulfillment = OrderFulfillment(inventory)
order_fulfillment.fulfill(order_req.name, order_req.address, order_req.item_ids)

# Logs:
# Charging card with name danny
# Inserting order into database
# Reducing inventory of 123 by 1
# Reducing inventory of 423 by 1
# Reducing inventory of 555 by 1
# Reducing inventory of 989 by 1
