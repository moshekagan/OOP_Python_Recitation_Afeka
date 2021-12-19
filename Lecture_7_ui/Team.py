class Team:
    def __init__(self, name, logo_url):
        self.name = name
        if not logo_url:
            self.logo_url = "https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-shield-20.png"
        self.logo_url = logo_url
        self.players = []

    def get_player(self, person_id):
        for player in self.players:
            if player.person_id == person_id:
                return player

        return None

    def get_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

        return None

    def add_player(self, player):
        if player is None:
            return False

        if self.get_player(player.person_id) is None:  # there is not player with same id in the team already
            self.players.append(player)
            player.set_team(self)
            return True

        return False

    def __str__(self):
        res = f"---- {self.name} ---- ({self.logo_url})\n"

        for player in self.players:
            res += f"{player}\n"

        return res

    def __repr__(self):
        return self.__str__()
