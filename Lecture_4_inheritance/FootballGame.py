from Lecture_4_inheritance.Game import Game


FIRST_HALF = 1
SECOND_HALF = 2


class FootballGame(Game):
    def __init__(self, team_a, team_b, game_date):
        super().__init__(team_a, team_b, game_date)
        self.half_1_score_a = 0
        self.half_1_score_b = 0

        self.half_2_score_a = 0
        self.half_2_score_b = 0

    def set_quart(self, quart, score_a, score_b):
        if quart == FIRST_HALF:
            self.half_1_score_a = score_a
            self.half_1_score_b = score_b
        elif quart == SECOND_HALF:
            self.half_2_score_a = score_a
            self.half_2_score_b = score_b

    def get_score_of_quart(self, quart):
        if quart == FIRST_HALF:
            return self.half_1_score_a, self.half_1_score_b
        elif quart == SECOND_HALF:
            return self.half_2_score_a, self.half_2_score_b
