import csv

from home_work.buy_a_car.Customer import Customer
from home_work.buy_a_car.Vehicle import Vehicle


class Store:
    def __init__(self, vehicles_csv_file_name, customers_csv_file_name):
        self.vehicles = self._create_vehicles_from_csv_file(vehicles_csv_file_name)
        self.customers = self._create_customers_from_csv_file(customers_csv_file_name)

    def _create_vehicles_from_csv_file(self, csv_file_name):
        vehicles = []

        with open(csv_file_name) as csvfile:
            read = csv.reader(csvfile)

            next(read)  # ignore fist line in the csv
            for row in read:
                vehicle = Vehicle(row)
                vehicles.append(vehicle)

        return vehicles

    def _create_customers_from_csv_file(self, csv_file_name):
        customers = []

        with open(csv_file_name) as csvfile:
            read = csv.reader(csvfile)

            next(read)  # ignore fist line in the csv
            for row in read:
                customer = Customer(row)
                customers.append(customer)

        return customers

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def get_vehicle(self, licence_plate):
        for vehicle in self.vehicles:
            if vehicle.licence_plate == licence_plate:
                return vehicle

        return None

    def add_vehicle(self, vehicle):
        # Check if already exist vehicle with same licence plate
        if self.get_vehicle(vehicle.licence_plate) is not None:
            return False

        self.vehicles.append(vehicle)
        return True

    def remove_vehicle(self, licence_plate):
        # Check if already exist vehicle with same licence plate
        vehicle = self.get_vehicle(licence_plate)
        if vehicle is not None:
            self.vehicles.remove(vehicle)
            return True

        return False

    def get_all_by_manufacturer(self, manufacturer):
        vehicles_by_manufacturer = []

        for vehicle in self.vehicles:
            if vehicle.manufacturer == manufacturer:
                vehicles_by_manufacturer.append(vehicle)

        return vehicles_by_manufacturer

    def get_all_by_price_under(self, price):
        vehicles_by_price = []

        for vehicle in self.vehicles:
            if vehicle.price < price:
                vehicles_by_price.append(vehicle)

        return vehicles_by_price

    def print_vehicles_list(self, vehicles):
        for vehicle in vehicles:
            vehicle.print_me()

    def get_most_expensive_vehicle(self):
        if len(self.vehicles) == 0:
            return None

        most_expensive_vehicle = self.vehicles[0]

        for vehicle in self.vehicles:
            if vehicle.price > most_expensive_vehicle.price:
                most_expensive_vehicle = vehicle

        return most_expensive_vehicle

    def print_customers(self):
        for customer in self.customers:
            print(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer

        return None

    def add_customer(self, customer):
        # Check if already exist customer with same id
        if not self.get_customer(customer.customer_id):
            return False

        self.vehicles.append(customer)
        return True

    def remove_customer(self, customer_id):
        customer = self.get_customer(customer_id)
        if customer is not None:
            self.customers.remove(customer)
            return True

        return False
