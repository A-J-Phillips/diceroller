from random import randint
from tkinter import *
from windows import win_roll_result
from dice_functions import fun_increment_dice, fun_reset_dice, fun_count_dice, fun_call_dice_rolls
from dice_class import Dice

root = Tk()
root.title("Dice Roller")
root.geometry("600x400")

lbl_welcome = Label(root, text="Welcome to the dice roller application.", pady=20).grid(column=3, row=0, columnspan=5)

# A set of buttons and entry boxes used to select the number of dice to roll.
# Although the .grid can be appended after the widget, it was causing errors so I've moved placement code
# on a seperate line.
# Entry widgets are defined before buttons so that functions can be called relating to the entry widgets
# Entry boxes for dice selection.

ent_d4 = Entry(root)
ent_d4.grid(column=1, row=1)
ent_d4.insert(0, 0)

ent_d6 = Entry(root)
ent_d6.grid(column=1, row=2)
ent_d6.insert(0, 0)

ent_d8 = Entry(root)
ent_d8.grid(column=1, row=3)
ent_d8.insert(0, 0)

ent_d10 = Entry(root)
ent_d10.grid(column=1, row=4)
ent_d10.insert(0, 0)

ent_d12 = Entry(root)
ent_d12.grid(column=1, row=5)
ent_d12.insert(0, 0)

ent_d20 = Entry(root)
ent_d20.grid(column=1, row=6)
ent_d20.insert(0, 0)

ent_d100 = Entry(root)
ent_d100.grid(column=1, row=7)
ent_d100.insert(0, 0)

# Creating dice objects using the Dice class for each die in the set, then storing them in a tuple to be passed
# to functions.
d4 = Dice(4, 0)
d6 = Dice(6, 0)
d8 = Dice(8, 0)
d10 = Dice(10, 0)
d12 = Dice(12, 0)
d20 = Dice(20, 0)
d100 = Dice(100, 0)
dice_types = (d4, d6, d8, d10, d12, d20, d100)

# Buttons to increment the dice counters
btn_d4 = Button(root, text="D4", padx=20, command=lambda: fun_increment_dice(ent_d4, d4))
btn_d4.grid(column=0, row=1, padx=10, pady=5)

btn_d6 = Button(root, text="D6", padx=20, command=lambda: fun_increment_dice(ent_d6, d6))
btn_d6.grid(column=0, row=2, padx=10, pady=5)

btn_d8 = Button(root, text="D8", padx=20, command=lambda: fun_increment_dice(ent_d8, d8))
btn_d8.grid(column=0, row=3, padx=10, pady=5)

btn_d10 = Button(root, text="D10", padx=20, command=lambda: fun_increment_dice(ent_d10, d10))
btn_d10.grid(column=0, row=4, padx=10, pady=5)

btn_d12 = Button(root, text="D12", padx=20, command=lambda: fun_increment_dice(ent_d12, d12))
btn_d12.grid(column=0, row=5, padx=10, pady=5)

btn_d20 = Button(root, text="D20", padx=20, command=lambda: fun_increment_dice(ent_d20, d20))
btn_d20.grid(column=0, row=6, padx=10, pady=5)

btn_d100 = Button(root, text="D100", padx=20, command=lambda: fun_increment_dice(ent_d100, d100))
btn_d100.grid(column=0, row=7, padx=10, pady=5)

# A list of the entry box vairables to pass to different functions.
dice_entry_boxes = (ent_d4, ent_d6, ent_d8, ent_d10, ent_d12, ent_d20, ent_d100)

# A button that rolls the selected number of dice.
btn_roll = Button(root, text="ROLL!!!", command=lambda: win_roll_result(dice_types))
btn_roll.grid(column=5, row=3, padx=40)

# A button that stores the entry boxes in a list, sends that list to the reset dice function, and sets all of the
# dice counter entry boxes to 0.
btn_clear = Button(root, text="Clear Dice\nSelection", command=lambda: fun_reset_dice(dice_entry_boxes, dice_types))
btn_clear.grid(column=0, row=8, columnspan=2)

# The mainloop signifies the end of the program.
root.mainloop()