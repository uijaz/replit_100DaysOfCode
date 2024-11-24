# Day 31 - Project Day: Create User Interfaces with Color
import os, time
os.system("clear")

# Generates coloured text
def cT(text, colour):
    # Dictionary of ANSI escape codes for different colors
    colours_dict = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    colour_code = colours_dict.get(colour, colours_dict["reset"])    
    return f"{colour_code}{text}{colours_dict['reset']}"

space = " "

while True:
  # Interface 1
  print(f"{space * 10}{cT('=', 'red')}{cT('=', 'reset')}{cT('=', 'blue')}{space * 1}{cT('Music App', 'yellow')}{space * 1}{cT('=', 'blue')}{cT('=', 'reset')}{cT('=', 'red')}")
  print()
  print(f"🔥▶️{space * 3}{cT('Radio Gaga', 'white')}")
  print(f"{space * 6}{cT('Queen', 'yellow')}")
  print()
  print()
  print(f"{space * 0}{cT('PREV', 'yellow')}")
  print(f"{space * 6}{cT('NEXT', 'green')}")
  print(f"{space * 12}{cT('PAUSE', 'magenta')}")

  time.sleep(3)
  os.system("clear")

  # Interface 2
  print(f"{space * 14}{cT('WELCOME TO', 'reset')}")
  print(f"{space * 10}{cT('-', 'blue')}{cT('-', 'blue')}{space * 3}{cT('ARM BOOK', 'blue')}{space * 3}{cT('-', 'blue')}{cT('-', 'blue')}")
  print()
  print(f"{space * 11}{cT('Definitely not rip off of', 'yellow')}")
  print(f"{space * 16}{cT('a certain other social', 'yellow')}")
  print(f"{space * 22}{cT('networking site.', 'yellow')}")
  print()
  print(f"{space * 16}{cT('Honest.', 'red')}")
  print()
  print(f"{space * 15}{cT('Username:', 'white')}")
  print(f"{space * 15}{cT('Password:', 'white')}")

  time.sleep(3)
  os.system("clear")