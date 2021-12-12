from tkinter import *

from Lecture_6_ui.League import League
from Lecture_6_ui.Team import Team


league = League()


def handel_create_team_click():
    text = f"You need to enter a team name!"
    fg = "red"

    if team_name_input.get():
        team = Team(team_name_input.get())

        res = league.add_team(team)
        if res:
            text = f"Created new team: {team.name}!"
            fg = "green"

            new_team_lbl = Label(frame, text=team.name)
            new_team_lbl.grid(row=len(league.teams)+4, column=0, sticky='nsew')
            frame.rowconfigure(len(league.teams))

            print(league.teams)
        else:
            text = f"Team {team.name} already exist"

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

frame = Frame(win)
frame.columnconfigure(1, weight=3)
frame.grid(row=5, column=0, sticky='nsew', rowspan=2)

win.mainloop()
print("App end")


