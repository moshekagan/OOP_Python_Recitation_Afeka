class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def get_player(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                return player

        return None

    def add_player(self, player):
        if player is None:
            return False

        if self.get_player(player.player_id) is None:  # there is not player with same id in the team already
            self.players.append(player)
            player.set_team(self)
            return True

        return False

    def __str__(self):
        res = f"---- {self.name} ----\n"

        for player in self.players:
            res += f"{player}\n"

        return res

    def __repr__(self):
        return self.__str__()
