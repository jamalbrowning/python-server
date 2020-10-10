from models.customer import Customer
CUSTOMERS = [
    Customer(1,"Hannah Hall", "NSS", 1, 4),
    Customer(2, "Brian Neal", "NSS Day",1, 2),
    Customer(3, "Mitchell Blom", "NSS Evening", 2,1)
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer.id == id:
            requested_customer = customer
    
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1].id
    new_id = max_id + 1
    customer.id = new_id
    CUSTOMERS.append(customer['id'], customer['name'], customer['business'], customer['location_id'],customer['customer_id'])

    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer.id == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer.id == id:
            CUSTOMERS[index] = CUSTOMERS(new_customer['id'], new_customer['name'], new_customer['business'],new_customer['location_id'], new_customer['customer_id'])
            break
