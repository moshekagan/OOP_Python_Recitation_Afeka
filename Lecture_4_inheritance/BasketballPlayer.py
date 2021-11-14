from Lecture_4_inheritance.Player import Player


class BasketballPlayer(Player):
    def __init__(self, name, person_id, birth_year, height, position, shirt_num):
        super().__init__(name, person_id, birth_year, height, position, shirt_num)
        self.rebounds = 0

    def print_me(self):
        super().print_me()
        print(f"rebounds: {self.rebounds}")

    def __str__(self):
        back = super().__str__()
        return f"{back}, {self.rebounds}"

    def add_2_points(self):
        self.add_points(2)

    def add_3_points(self):
        self.add_points(3)
