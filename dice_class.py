from tkinter import *
from random import randint

class Dice:
    """A class that represents dice and their functions."""

    def __init__(self, sides, quantity):
        """Initialising a dice object."""
        self.sides = sides
        self.quantity = int(quantity)

    def roll_dice(self, window):
        """A class function to roll selected dice. window arg refers to what window the results will be put into."""
        dice_rolled = 0
        print(self.quantity)
        while dice_rolled < self.quantity:
            roll = randint(1, self.sides)
            if roll == self.sides:
                lbl_roll = Label(window, text=f"You rolled a D{self.sides}, the result is {roll}.\n"
                                              f"That's a CRITICAL!!!")
                lbl_roll.pack()
            else:
                lbl_roll = Label(window, text=f"You rolled a D{self.sides}, the result is {roll}!")
                lbl_roll.pack()
            dice_rolled += 1

