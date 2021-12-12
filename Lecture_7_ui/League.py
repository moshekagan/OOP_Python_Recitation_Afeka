import csv

from Lecture_6_ui.BasketballGame import BasketballGame
from Lecture_6_ui.BasketballPlayer import BasketballPlayer
from Lecture_6_ui.Team import Team


class TeamNotExistError(Exception):
    pass


class League:
    def __init__(self):
        self.teams = []
        self.games = []

    def import_teams(self, teams_file_name, players_file_name):
        self._generate_teams(teams_file_name)
        self._generate_players(players_file_name)

    def _generate_players(self, players_file_name):
        with open(players_file_name, newline='') as csvfile:
            read = csv.reader(csvfile)

            next(read)  # ignore fist line in the csv
            for row in read:
                player_team_name = row[17]
                player = BasketballPlayer(name=row[0],
                                          person_id=(row[3]),
                                          birth_year=row[10],
                                          height=int(float(row[16])),
                                          position=row[7],
                                          shirt_num=row[8],
                                          profile_url=row[11])

                team = self.get_team_by_name(player_team_name)

                if team is not None:
                    team.add_player(player)
                else:
                    raise TeamNotExistError(f"Team {player_team_name} not exist in the league! Failed to add player [{player}]")

    def _generate_teams(self, teams_file_name):
        with open(teams_file_name, newline='') as csvfile:
            read = csv.reader(csvfile)

            next(read)  # ignore fist line in the csv
            for row in read:
                team = Team(row[1], row[2])
                self.add_team(team)

    def get_team_by_name(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team

        return None

    def _is_team_exist(self, team):
        return self.get_team_by_name(team.name) is not None

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
