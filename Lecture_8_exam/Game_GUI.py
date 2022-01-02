from tkinter import ttk
from tkinter import *

from tkinter import messagebox

from Lecture_8_exam.Game import *


def start_game():
    lg=List_Of_Games()
    b1=Ball_Game("basketball",7,2)
    b2=Ball_Game("VollBall",8,6)
    d1=Board_Game("Katan",10,6)
    d2=Board_Game("Splendor",7,4)
    lg.add_game(b1)
    lg.add_game(d1)
    lg.add_game(b2)
    lg.add_game(d2)
    return lg


def handel_find_game_click():
    try:
        num_of_players = int(como_ages.get())
        is_raining = is_raining_value.get()
        game = lg.get_next_game(num_of_players, is_raining)

        if game is not None:
            messagebox.showinfo(title="Your next game is:",message=game)
        print(str(game))
    except ValueError:
        print("number of players didnt choose!")


lg=start_game()
wind=Tk()
wind.geometry('400x500')

players_label = Label(text="How many players?")
players_label.grid(row=0, column=0)

como_ages = ttk.Combobox(values=[i for i in range(1, 9)])
como_ages.grid(row=0, column=1)

find_game_btn = Button(text="Find Game", command=handel_find_game_click)
find_game_btn.grid(row=1, column=0)

is_raining_value = BooleanVar(value=True)
is_raining_checkbox = ttk.Checkbutton(wind, text="Is raining?", var=is_raining_value)
is_raining_checkbox.grid(row=1, column=1)

wind.mainloop()
