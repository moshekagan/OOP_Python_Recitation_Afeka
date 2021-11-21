import random


class Customer:
    def __init__(self, data):
        self.customer_id = int(data[0])
        self.name = data[1]
        self.address = data[2]
        self.phone_number = self._validate_phone_number(data[3])
        self.gender = self._validate_gender(data[4])

    def _validate_phone_number(self, number):
        number = number.strip()     # remove spaces

        if len(number) != 10:
            new_number_without_prefix = random.randrange(100000000, 999999999)
            number = f"0{new_number_without_prefix}"

        return number

    def _validate_gender(self, gender):
        gender_types = ["M", "F"]
        gender = gender.upper().strip()

        gender = " F"   # gender with space
        gender = gender.strip()     # now gender is: "F"

        if gender not in gender_types:
            index_in_gender_type = random.randrange(0, len(gender_types))
            gender = gender_types[index_in_gender_type]

        return gender

    def print_me(self):
        print(f"---- {self.customer_id} ----")
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"phone_number: {self.phone_number}")
        print(f"gender: {self.gender}")

    def __str__(self):
        return f"{self.customer_id}, {self.name}, {self.address}, {self.phone_number}, {self.gender}"

    def __repr__(self):
        return self.__str__()
