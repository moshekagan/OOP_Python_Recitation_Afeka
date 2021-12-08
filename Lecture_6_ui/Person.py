class Person:
    def __init__(self, name, person_id, birth_year):
        self.person_id = person_id
        self.name = name
        self.birth_year = birth_year

    def print_me(self):
        print()
        print(f"---- {self.person_id} ----")
        print(f"name: {self.name}")
        print(f"birth year: {self.birth_year}")

    def __str__(self):
        return f"{self.person_id}, {self.name}, {self.birth_year}"

    def __repr__(self):
        return self.__str__()
