# day31_100days.py
import os, time
from utils_100days import changeColour

os.system("clear")

space = " "

while True:
    # Interface 1
    print(f"{space * 10}{changeColour('=', 'red')}{changeColour('=', 'white')}{changeColour('=', 'blue')}{space * 1}{changeColour('Music App', 'yellow')}{space * 1}{changeColour('=', 'blue')}{changeColour('=', 'white')}{changeColour('=', 'red')}")
    print()
    print(f"🔥▶️{space * 3}{changeColour('Radio Gaga', 'white')}")
    print(f"{space * 6}{changeColour('Queen', 'yellow')}")
    print()
    print()
    print(f"{space * 0}{changeColour('PREV', 'yellow')}")
    print(f"{space * 6}{changeColour('NEXT', 'green')}")
    print(f"{space * 12}{changeColour('PAUSE', 'magenta')}")

    time.sleep(3)
    os.system("clear")

    # Interface 2
    print(f"{space * 14}{changeColour('WELCOME TO', 'white')}")
    print(f"{space * 10}{changeColour('-', 'blue')}{changeColour('-', 'blue')}{space * 3}{changeColour('ARM BOOK', 'blue')}{space * 3}{changeColour('-', 'blue')}{changeColour('-', 'blue')}")
    print()
    print(f"{space * 11}{changeColour('Definitely not rip off of', 'yellow')}")
    print(f"{space * 16}{changeColour('a certain other social', 'yellow')}")
    print(f"{space * 22}{changeColour('networking site.', 'yellow')}")
    print()
    print(f"{space * 16}{changeColour('Honest.', 'red')}")
    print()
    print(f"{space * 15}{changeColour('Username:', 'white')}")
    print(f"{space * 15}{changeColour('Password:', 'white')}")

    time.sleep(3)
    os.system("clear")