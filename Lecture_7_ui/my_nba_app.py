from tkinter import messagebox
from tkinter import *
import tkinter.ttk as ttk

from Lecture_7_ui.League import League


def _is_valid_in_range(num, min_num, max_num):
    return min_num <= num <= max_num


def validate_date():
    try:
        day = int(day_input.get())
        month = int(month_input.get())
        year = int(year_input.get())

        if not _is_valid_in_range(day, 1, 30):
            status_label.configure(text="Day must be between 1-30", fg="red")
            return None

        if not _is_valid_in_range(month, 1, 12):
            status_label.configure(text="Month must be between 1-12", fg="red")
            return None

        if not _is_valid_in_range(year, 2021, 2022):
            status_label.configure(text="Year must be between 2021-2022", fg="red")
            return None

        return (day, month, year)
    except ValueError:
        status_label.configure(text="Date must by valid!", fg="red")
        return None


def handel_create_game_click():
    team_a = teams_combo_1.get()
    team_b = teams_combo_2.get()

    if not team_a or not team_b:
        status_label.configure(text="You need to select 2 teams!", fg="red")
    elif team_a == team_b:
        status_label.configure(text="You need to select different teams!", fg="red")
    else:
        date = validate_date()
        if date is None:
            return

        game = league.generate_game(team_a, team_b, date)
        status_label.configure(text=f"New game created: {game}", fg="green")


def handel_select_team_click():
    team_name = display_teams_combo.get()
    if not team_name:
        return

    team = league.get_team_by_name(team_name)
    players = [f"{player.shirt_num}.\t{player.name}" for player in sorted(team.players, key=lambda p: p.shirt_num)]
    display_players_combo.configure(values=players)
    status_label.configure(text=f"{team_name} Selected! Take a look in the players list...", fg="green")


def handel_select_player_click():
    player_name = display_players_combo.get()
    if not player_name:
        return

    r = player_name.split(".")
    player_name = r[1].strip()

    team_name = display_teams_combo.get()
    if not team_name:
        return

    team = league.get_team_by_name(team_name)
    player = team.get_player_by_name(player_name)
    status_label.configure(text=f"{player.name} Selected!", fg="green")
    messagebox.showinfo(title=f"#{player.shirt_num} - {player.name}", message=f"#{player.shirt_num}\n name: {player.name}\n birth_year: {player.birth_year}\n  height: {player.height}\n position: {player.position}\n \nprofile_url:\n {player.profile_url}\n")


"""
Creating our League and import all data from CSVs files
This will manage all the business logic of the app
"""
league = League()
league.import_teams("NBA_all_teams.csv", "NBA_roster_info_all_players.csv")


"""
Creating app Window
With title and header label
"""
win = Tk()
win.title("My NBA League")
win.geometry("1000x600")
title = Label(win, text="My NBA App", font=("Ariel Bold", 50), fg="purple")
title.grid(column=0, row=0)

status_label = Label(win, text="Welcome to my NBA app")
status_label.grid(column=0, row=1)


"""
Feature 1 -
Creating new game - 
Need to select 2 teams and inserting a valid date as a input
"""
feature_label = Label(win, text="Create new game:", fg="blue")
feature_label.grid(column=0, row=2)

teams_combo_1 = ttk.Combobox(win, values=league.teams_names())
teams_combo_1.grid(row=3, column=0)

teams_combo_2 = ttk.Combobox(win, values=league.teams_names())
teams_combo_2.grid(row=3, column=1)

day_label = Label(win, text="day")
day_input = Entry()
day_label.grid(row=4, column=0)
day_input.grid(row=5, column=0)

month_label = Label(win, text="month")
month_input = Entry()
month_label.grid(row=4, column=1)
month_input.grid(row=5, column=1)

year_label = Label(win, text="year")
year_input = Entry()
year_label.grid(row=4, column=2)
year_input.grid(row=5, column=2)

create_game_btn = Button(win, text="Create Game", width=10, height=2, command=handel_create_game_click)
create_game_btn.grid(row=5, column=3)


"""
Feature 2 -
Selecting a team and display all player in combobox
Can Select Player and display his personal info in a messagebox
"""
feature_label = Label(win, text="Teams info:", fg="blue")
feature_label.grid(row=7, column=0)

display_teams_combo = ttk.Combobox(win, values=league.teams_names())
display_teams_combo.grid(row=8, column=0)

display_team_btn = Button(win, text="Select team", width=10, height=2, command=handel_select_team_click)
display_team_btn.grid(row=8, column=1)

display_players_combo = ttk.Combobox(win, values=[])
display_players_combo.grid(row=8, column=2)

display_team_btn = Button(win, text="Display player", width=10, height=2, command=handel_select_player_click)
display_team_btn.grid(row=8, column=3)


# Start app!
win.mainloop()
print("App end")
