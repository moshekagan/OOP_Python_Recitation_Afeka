from Lecture_5_exceptions.League import League
from Lecture_5_exceptions.Team import Team

def main():
    basketball_league = League()

    macabbi = Team("Maccabi Tel-Aviv")
    happpoel = Team("Happoel Tel-Aviv")
    elizor = Team("Elizur Tel-Aviv")


    basketball_league.add_team(macabbi)
    basketball_league.add_team(happpoel)

    game_1 = basketball_league.generate_game(macabbi, happpoel, (1, 1, 2022))
    game_2 = basketball_league.generate_game(happpoel, elizor, (7, 1, 2022))


if __name__ == '__main__':
    main()
