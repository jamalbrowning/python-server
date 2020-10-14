class Customer():

    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        

new_customer = Customer("Emily Lemmon","Hannah Hall", "something@gmail.com", 1, 4)


# {
#         "id": 1,
#         "name": "Hannah Hall",
#         "business": "NSS",
#         "locationId": 1,
#         "customerId": 4
#     },
