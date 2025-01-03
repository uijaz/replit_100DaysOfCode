# utils_100days.py
# Library of commonly used utility functions in the 100days project

import time
import random

# day26_100days
def printText(text):
  """
  Prints text one character at a time

  Agrs:
  text: str: Text to be printed
  """
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)
  print()

# day24_100days
# day25_100days
# day27_100days
# day28_100days
def diceRoll(numberOfSides):
  """
  Rolls a dice with a given number of sides

  Args:
  numberOfSides: int: Number of sides of the dice

  Returns:
  int: Random number between 1 and the number of sides
  """
  return random.randint(1, numberOfSides)

# day31_100days
# day35_100days
# day42_100days
# day45_100days
# day46_100days
# day51_100days
# day55_100days
def changeColour(text, colour):
    """
    Changes colour of the text

    Args:
    text: str: Text to be coloured
    colour: str: Colour of the text

    Returns:
    str: Coloured text
    """
    colours = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    colour_code = colours.get(colour.lower(), colours["reset"])
    return f"{colour_code}{text}{colours['reset']}"