import random

MIN_LICENCE_PLATE = 0
MAX_LICENCE_PLATE = 99999999
MIN_YEAR = 1900
MAX_YEAR = 2022
MIN_PRICE = 1000
MAX_PRICE = 3000000


class Vehicle:
    def __init__(self, data):
        self.licence_plate = self._validate_number_in_range(data[0], MIN_LICENCE_PLATE, MAX_LICENCE_PLATE)
        self.vehicle_type = data[1]
        self.manufacturer = data[2]
        self.model = data[3]
        self.year = self._validate_number_in_range(data[4], MIN_YEAR, MAX_YEAR)
        self.price = self._validate_number_in_range(data[5], MIN_PRICE, MAX_PRICE)

    def _validate_number_in_range(self, num, min_range, max_range):
        num = int(num)

        if num < min_range or num > max_range:
            num = random.randrange(min_range, max_range)

        return num

    def print_me(self):
        print(f"---- {self.licence_plate} ----")
        print(f"type: {self.vehicle_type}")
        print(f"manufacturer: {self.manufacturer}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")
        print(f"price: {self.price} NIS")

    def __str__(self):
        return f"{self.licence_plate}, {self.vehicle_type}, {self.manufacturer}, {self.model}, {self.year}, {self.price}"

    def __repr__(self):
        return self.__str__()

