class Game:
    def __init__(self, name, min_age, players_num):
        self.name = name
        self.min_age = min_age
        self.players_num = players_num
        self.is_boring = False

    def __str__(self):
        return f"{self.name} is a game for {self.players_num} players"

    def __repr__(self):
        return self.__str__()

    def is_borring(self):
        return self.is_boring

    def play_to_much(self):
        self.is_boring = True


class Board_Game(Game):
    def __init__(self, name, min_age, players_num):
        super().__init__(name, min_age, players_num)


class Ball_Game(Game):
    def __init__(self, name, min_age, players_num):
        super().__init__(name, min_age, players_num)

    def __str__(self):
        return super().__str__() + " you need a ball for this game :)"


class List_Of_Games:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def __str__(self):
        return str(self.games)

    def __repr__(self):
        return self.__str__()

    def get_next_game(self, num_of_players, is_rain):
        for game in self.games:
            if not game.is_borring() and game.players_num > num_of_players:
                if is_rain:
                    if isinstance(game, Board_Game):
                        return game
                else:
                    return game

        return None


if __name__ == '__main__':
    lg = List_Of_Games()
    b1 = Ball_Game("basketball", 7, 2)
    b2 = Ball_Game("VollBall", 8, 6)
    d1 = Board_Game("Katan", 10, 6)
    d2 = Board_Game("Splendor", 7, 4)
    lg.add_game(b1)
    lg.add_game(d1)
    lg.add_game(b2)
    lg.add_game(d2)
    print(lg)

    print(lg.get_next_game(4, False))
    print(lg.get_next_game(4, False))
    print(lg.get_next_game(1, False))
    print(lg.get_next_game(1, True))
    d1.play_to_much()
    print(lg.get_next_game(1, True))
    print(lg.get_next_game(4, False))

