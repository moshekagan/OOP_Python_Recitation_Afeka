class Game:
    def __init__(self, team_a, team_b, game_date):
        self.team_a = team_a
        self.team_b = team_b
        self.score_a = 0
        self.score_b = 0
        self.game_date = game_date

    def set_score(self, score_a, score_b):
        self.score_a = score_a
        self.score_b = score_b

    def get_winner(self):
        if self.score_a > self.score_b:
            return 1
        elif self.score_a < self.score_b:
            return 2
        else:
            return 0

    def __str__(self):
        return f"{self.team_a.name} - {self.score_a} : {self.score_b} - {self.team_b.name} ({self.game_date[0]},{self.game_date[1]},{self.game_date[2]})"
