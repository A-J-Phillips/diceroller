"""A module to store all of the windows for the program"""
from tkinter import *
from random import randint
from dice_functions import fun_call_dice_rolls
from dice_class import Dice

def win_roll_result(dice_types):
    """A window to display the dice roll results."""
    result = Tk()
    result.title("Result Screen")
    result.geometry("500x400")

    fun_call_dice_rolls(dice_types, result)

    result.mainloop()