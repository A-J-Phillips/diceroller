from random import randint
from tkinter import *
from dice_class import Dice

"""The functions for the various dice"""


def fun_increment_dice(dice_type, dice_object):
    """A function to increment the dice counters"""
    num = int(dice_type.get())
    new_num = num + 1
    dice_type.delete(0, END)
    dice_type.insert(0, new_num)

    fun_count_dice(num, dice_object)


def fun_count_dice(num, dice_object):
    """A function that counts how many dice are selected."""
    dice_object.quantity = num
    dice_object.quantity += 1


def fun_reset_dice(dice, dice_objects):
    """A Function to reset the dice incrementers."""
    for die in dice:
        die.delete(0, END)
        die.insert(0, 0)

    for object in dice_objects:
        object.quantity = 0


def fun_call_dice_rolls(dice, window):
    """A function that calls the roll_dice class function for each dice type."""
    for die in dice:
        die.roll_dice(window)
