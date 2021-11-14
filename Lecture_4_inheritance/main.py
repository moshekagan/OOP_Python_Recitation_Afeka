from Lecture_4_inheritance.BasketballPlayer import BasketballPlayer
from Lecture_4_inheritance.Coach import Coach
from Lecture_4_inheritance.FootballPlayer import FootballPlayer
from Lecture_4_inheritance.Person import Person
from Lecture_4_inheritance.Player import Player
from Lecture_4_inheritance.Team import Team


def main():
    simple_person = Person("Ehud Banai", 111, 1960)
    print(simple_person)
    print()

    generic_player = Player("Kasparov", 222, 170, "Chess", 1940, 0)
    print(generic_player)
    print()

    basketball_player = BasketballPlayer("Curry", 333, 1988, 192, "PG", 30)
    print(basketball_player)
    print()

    football_player = FootballPlayer("Messi", 444, 1985, 160, "Playmeker", 10)
    print(football_player)
    print()

    coach = Coach("Pini", 555, 1950, 40, "Head Coach")
    print(coach)
    print()

    macabbi = Team("Golden-State Warriors")
    macabbi.add_player(basketball_player)

    simple_person.print_me()
    generic_player.print_me()
    basketball_player.print_me()
    football_player.print_me()


if __name__ == '__main__':
    main()
