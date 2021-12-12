from Lecture_6_ui.League import League


def main():
    league = League()

    league.import_teams("NBA_all_teams.csv", "NBA_roster_info_all_players.csv")

    ws_team = league.get_team_by_name('Washington Wizards')
    print(ws_team)
    print(ws_team.players[0])
    print(league)


if __name__ == '__main__':
    main()
