from Lecture_5_exceptions.BasketballGame import BasketballGame
from Lecture_5_exceptions.BasketballPlayer import BasketballPlayer
from Lecture_5_exceptions.SportLeagueError import SportLeagueError
from Lecture_5_exceptions.Team import Team


def main():
    macabbi = Team("Maccabi Tel-Aviv")
    happpoel = Team("Happoel Tel-Aviv")

    derbi_game = BasketballGame(macabbi, happpoel, (29, 11, 2021))

    try:
        derbi_game.set_quart(1, 10, 12)
        derbi_game.set_quart(2, 14, 11)
        derbi_game.set_quart(3, 16, 12)
        derbi_game.set_quart(4, 15, 18)

        # derbi_game.set_quart(5, 15, 18)
        print(derbi_game)

        basketball_player = BasketballPlayer("Jorden", 111, 1970, 203, "Shooter", 23)
        print(basketball_player)
    except SportLeagueError as e:
        print(e)


if __name__ == '__main__':
    main()
