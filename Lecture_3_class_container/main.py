from Lecture_3_class_container.Player import Player
from Lecture_3_class_container.Team import Team


def main():
    macabbi = Team("Maccabi Tel-Aviv")

    player_1 = Player("Antony Parker", 111, 202, "SG", 1975, 8)
    player_2 = Player("Saras", 222, 193, "PG", 1976, 13)
    player_3 = Player("Baston", 333, 208, "PF", 1976, 5)

    macabbi.add_player(player_1)
    macabbi.add_player(player_2)

    print(macabbi)

    print(player_1.team)
    print(player_2.team)
    print(player_3.team)


if __name__ == '__main__':
    main()
