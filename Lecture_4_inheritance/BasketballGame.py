from Lecture_4_inheritance.Game import Game


FIRST_QUARTER = 1
SECOND_QUARTER = 2
THIRD_QUARTER = 3
FOURTH_QUARTER = 4


class BasketballGame(Game):

    def __init__(self, team_a, team_b, game_date):
        super().__init__(team_a, team_b, game_date)
        self.qut_1_score_a = 0
        self.qut_1_score_b = 0

        self.qut_2_score_a = 0
        self.qut_2_score_b = 0

        self.qut_3_score_a = 0
        self.qut_3_score_b = 0

        self.qut_4_score_a = 0
        self.qut_4_score_b = 0

    def get_winner(self):
        if self.score_a > self.score_b:
            return 1
        elif self.score_a < self.score_b:
            return 2

    def set_quart(self, quart, score_a, score_b):
        if quart == FIRST_QUARTER:
            self.qut_1_score_a = score_a
            self.qut_1_score_b = score_b
        elif quart == SECOND_QUARTER:
            self.qut_2_score_a = score_a
            self.qut_2_score_b = score_b
        elif quart == THIRD_QUARTER:
            self.qut_3_score_a = score_a
            self.qut_3_score_b = score_b
        elif quart == FOURTH_QUARTER:
            self.qut_4_score_a = score_a
            self.qut_4_score_b = score_b

    def get_score_of_quart(self, quart):
        if quart == FIRST_QUARTER:
            return self.qut_1_score_a, self.qut_1_score_b
        elif quart == SECOND_QUARTER:
            return self.qut_2_score_a, self.qut_2_score_b
        elif quart == THIRD_QUARTER:
            return self.qut_3_score_a, self.qut_3_score_b
        elif quart == FOURTH_QUARTER:
            return self.qut_4_score_a, self.qut_4_score_b
