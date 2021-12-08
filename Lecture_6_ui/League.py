from Lecture_6_exceptions.BasketballGame import BasketballGame


class TeamNotExistError(Exception):
    pass


class League:
    def __init__(self):
        self.teams = []
        self.games = []

    def _is_team_exist(self, team):
        for t in self.teams:
            if t.name == team.name:
                return True

        return False

    def add_team(self, team):
        if not self._is_team_exist(team):
            self.teams.append(team)
            return True

        return False

    def generate_game(self, team_a, team_b, date):
        if not self._is_team_exist(team_a) or not self._is_team_exist(team_b):
           raise TeamNotExistError

        game = BasketballGame(team_a, team_b, date)
        self.games.append(game)

        return game
