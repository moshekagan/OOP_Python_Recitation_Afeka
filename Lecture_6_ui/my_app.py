from tkinter import *
import tkinter.ttk as ttk

from Lecture_6_ui.League import League
from Lecture_6_ui.Team import Team


league = League()


def handel_create_team_click():
    text = f"You need to enter a team name!"
    fg = "red"

    # Adding to combobox id checkbox is check
    if enable_add_team_value.get():
        if team_name_input.get():
            team = Team(team_name_input.get())

            res = league.add_team(team)
            if res:
                text = f"Created new team: {team.name}!"
                fg = "green"

                # Update label
                new_team_lbl = Label(frame, text=team.name)
                new_team_lbl.grid(row=len(league.teams)+4, column=0, sticky='nsew')

                # Add team name to combobox list
                teams_combo.configure(values=[t.name for t in league.teams])

                # Display all teams in a list (Bonus)
                frame.rowconfigure(len(league.teams))

                print(league.teams)
            else:
                text = f"Team {team.name} already exist"
    else:
        text = "You need to enable adding team..."
        fg = "orange"

    status_label.configure(text=text, fg=fg)


win = Tk()
# win.configure(background='pink')
win.title("Basketball League")
win.geometry("800x600")
title = Label(win, text="Teams", font=("Ariel Bold", 50), fg="purple")
title.grid(column=0, row=0)

status_label = Label(win, text="You didn't create a team yet...")
status_label.grid(column=0, row=1)

btn = Button(win, text="Create team", width=10, height=2, fg="blue", bg="pink", command=handel_create_team_click)
btn.grid(column=1, row=2)

team_name_input = Entry(win, width=15)
team_name_input.grid(column=0, row=2)
team_name_input.focus()

teams_combo = ttk.Combobox(win, values=[])
teams_combo.grid(row=5, column=0)

enable_add_team_value = BooleanVar(value=True)
enable_add_team_checkbox = ttk.Checkbutton(win, text="Enable add team", var=enable_add_team_value)
enable_add_team_checkbox.grid(row=6, column=0)

frame = Frame(win)
frame.columnconfigure(1, weight=3)
frame.grid(row=7, column=0, sticky='nsew', rowspan=2)

win.mainloop()
print("App end")


