from customers.customer_manager import CustomerManager
from customers.location_tracker import update_customer_location

# Initial dictionary of customers (students will enhance this later)
customers = {
    "cust_101": {"name": "Alice", "location": "New York", "purchases": ["Laptop", "Mouse"]},
    "cust_102": {"name": "Bob", "location": "Los Angeles", "purchases": ["Phone", "Charger"]},
    "cust_103": {"name": "Charlie", "location": "New York", "purchases": ["Tablet", "Headphones"]}
}

customer_manager = CustomerManager(customers)

print("\nAll Customers:")
customer_manager.display_customers()

# Filter customers by city
filtered_customers = customer_manager.filter_customers_by_city("New York")
print(filtered_customers)

# Unique locations are not yet implemented (students will add them)
print("\nUnique Locations:")
customer_manager.get_unique_locations()
update_customer_location(customers, "cust_102", "San Francisco")
print("\nUpdated Unique Locations:")
customer_manager.get_unique_locations()