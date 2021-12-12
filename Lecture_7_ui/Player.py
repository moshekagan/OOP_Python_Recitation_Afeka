from Lecture_6_ui.Person import Person


class Player(Person):
    def __init__(self, name, person_id, birth_year, height, position, shirt_num, profile_url):
        super().__init__(name, person_id, birth_year)
        self.height = height
        self.position = position
        self.shirt_num = shirt_num
        self.score = 0
        self.team = None
        if not profile_url:
            self.profile_url = "https://www.seekpng.com/png/full/514-5147412_default-avatar-icon.png"
        self.profile_url = profile_url

    def print_me(self):
        super().print_me()
        print(f"shirt: #{self.shirt_num}")
        print(f"height: {self.height}")
        print(f"position: {self.position}")
        print(f"score: {self.score}")

        if self.team is not None:
            print(f"team: {self.team.name}")

    def is_tall(self):
        if self.height >= 200:
            return True
        else:
            return False

    def __str__(self):
        back = super().__str__()
        return back + f", {self.height}, {self.position}, {self.shirt_num}, {self.score}, {self.profile_url}"

    def add_points(self, points):
        if points > 0:
            self.score += points

    def init_score(self):
        self.score = 0

    def print_score(self):
        print(f"#{self.shirt_num} - {self.score} points")

    def set_team(self, team):
        if self.team is not None:
            return False

        self.team = team
        return True
