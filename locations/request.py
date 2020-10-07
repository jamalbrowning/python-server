LOCATIONS = [
    {
        "id": 1,
        "name": "TEST1",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "TEST2",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "TEST3",
        "locationId": 2
    }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    
    return requested_location
