# This module should implement filtering using Dictionary Comprehensions
def filter_customers_by_city(customer_db, city):
    # creating a new dictionary with filtered customers 
    filtered_customers = {
        cust_id: details 
        for cust_id, details in customer_db.items() 
        if details["location"].lower() == city.lower()
        }

    if filtered_customers:
        print(f"\nCustomers in {city}:")
        return filtered_customers
    else:
        print(f"\nNo customers found in {city}.")
        return {}