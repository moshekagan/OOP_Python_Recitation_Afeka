from Lecture_5_exceptions.Player import Player
from Lecture_5_exceptions.SportLeagueError import SportLeagueError


class BasketballPlayer(Player):
    def __init__(self, name, person_id, birth_year, height, position, shirt_num):
        if position not in ["PG", "SG", "SF", "PF", "C"]:
            raise SportLeagueError(f"Invalid [{position}] position in BasketballPlayer!")

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
