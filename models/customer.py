class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, business, location_id, customer_id):
        self.id = id
        self.name = name
        self.business = business
        self.location_id = location_id
        self.customer_id = customer_id

new_customer = Customer(1,"Hannah Hall", "NSS", 1, 4)


# {
#         "id": 1,
#         "name": "Hannah Hall",
#         "business": "NSS",
#         "locationId": 1,
#         "customerId": 4
#     },
