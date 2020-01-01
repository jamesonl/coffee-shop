import uuid

cust_database = {}

class Customer(object):
    """docstring for Customer."""

    def __init__(self, guid, name, email, lifetime_orders_schedule):
        super(Customer, self).__init__()
        self.guid = uuid.uuid4()
