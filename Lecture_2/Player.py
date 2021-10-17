class Player:
    def __init__(self, name, player_id, height, positions, birth_year):
        self.name = name
        self.player_id = player_id
        self.height = height
        self.positions = positions
        self.birth_year = birth_year

    def print_me(self):
        print()
        print(f"---- {self.player_id} ----")
        print(f"name: {self.name}")
        print(f"height: {self.height}")
        print(f"positions: {self.positions}")
        print(f"birth year: {self.birth_year}")
