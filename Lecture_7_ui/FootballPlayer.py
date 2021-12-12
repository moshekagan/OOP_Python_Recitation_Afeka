from Lecture_5_exceptions.Player import Player


class FootballPlayer(Player):
    def __init__(self, name, person_id, birth_year, height, position, shirt_num):
        super().__init__(name, person_id, birth_year, height, position, shirt_num)
        self.yellow_cards = 0
        self.red_cards = 0

    def print_me(self):
        print()
        print(f"---- {self.person_id} ----")
        print(f"name: {self.name}")
        print(f"birth year: {self.birth_year}")
        print(f"shirt: #{self.shirt_num}")
        print(f"position: {self.position}")
        print(f"score: {self.score}")
        print(f"red cards: {self.red_cards}")
        print(f"yellow cards: {self.yellow_cards}")

    def __str__(self):
        back = super().__str__()
        return f"{back}, {self.yellow_cards}, {self.red_cards}"

    def add_red_card(self):
        self.red_cards += 1

    def add_yellow_card(self):
        self.yellow_cards += 1
