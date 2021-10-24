from Lecture_2.Player import Player


def main():
    player = Player("Antony Parker", 111, 202, "SG", 1975, 8)
    player.print_me()

    print()
    if player.is_tall():
        print(f"{player.name} is tall!")
    else:
        print(f"{player.name} is NOT tall!")

    print()
    player.add_2_points()
    player.print_score()

    player.add_3_points()
    player.print_score()

    player.init_score()
    player.print_score()


if __name__ == '__main__':
    main()
