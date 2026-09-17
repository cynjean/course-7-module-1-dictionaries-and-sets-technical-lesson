# This module should implement unique location tracking using Set Operations
# Track unique customer locations
def get_unique_locations(customer_db):
    customer_locations = {
        customer["location"]
        for customer in customer_db.values()
    }
    print("\nUnique Customer Locations:", customer_locations)
    return customer_locations

# Update a customer's location
def update_customer_location(customer_db, customer_id, new_location):
    if customer_id in customer_db:
        old_location = customer_db[customer_id]["location"]
        customer_db[customer_id]["location"] = new_location
        print(f"\nUpdated {customer_db[customer_id]['name']}'s location from {old_location} to {new_location}.")
    else:
        print("\nCustomer not found.")
