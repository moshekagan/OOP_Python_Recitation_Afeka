
class Player:
    def __init__(self, name, player_id, height, position, birth_year, shirt_num):
        self.name = name
        self.player_id = player_id
        self.height = height
        self.position = position
        self.birth_year = birth_year
        self.shirt_num = shirt_num
        self.score = 0
        self.team = None

    def print_me(self):
        print()
        print(f"---- {self.player_id} ----")
        print(f"shirt: #{self.shirt_num}")
        print(f"name: {self.name}")
        print(f"height: {self.height}")
        print(f"position: {self.position}")
        print(f"birth year: {self.birth_year}")

    def is_tall(self):
        if self.height >= 200:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.player_id}, {self.name}, {self.height}, {self.position}, {self.birth_year}, {self.shirt_num}, {self.score}"

    def __repr__(self):
        return self.__str__()

    def add_points(self, points):
        if points > 0:
            self.score += points

    def add_2_points(self):
        self.add_points(2)

    def add_3_points(self):
        self.add_points(3)

    def init_score(self):
        self.score = 0

    def print_score(self):
        print(f"#{self.shirt_num} - {self.score} points")

    def set_team(self, team):
        if self.team is not None:
            return False

        self.team = team
        return True
