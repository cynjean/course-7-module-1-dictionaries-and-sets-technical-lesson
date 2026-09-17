from customers.filters import filter_customers_by_city as filter_by_city
from customers.location_tracker import get_unique_locations as track_locations

class CustomerManager:
    def __init__(self, customers):
        self.customers = customers

    def display_customers(self):
        """Displays all customer records."""
        for cust_id, details in self.customers.items():
            print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")

    def filter_customers_by_city(self, city):
        """Placeholder for filtering customers (students will implement)."""
        return filter_by_city(self.customers, city)

    def get_unique_locations(self):
        """Placeholder for retrieving unique locations (students will implement)."""
        return track_locations(self.customers)
