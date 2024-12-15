#myGPTexperiment
# Day 42 - Project Day: MokéBeast

import os

def clear_screen():
    os.system('clear')

def change_colour(text, colour):
    colours_dict = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    colour_code = colours_dict.get(colour, colours_dict["reset"])
    return f"{colour_code}{text}{colours_dict['reset']}"

def choose_colour(type):
    type_lower = type.lower()
    if type_lower == 'fire':
        return 'red'
    elif type_lower == 'water':
        return 'blue'
    elif type_lower == 'air':
        return 'white'
    elif type_lower == 'earth':
        return 'green'
    else:
        return 'yellow'

def pretty_print(mokedex):
    print("🌟 Full Mokedex 🌟")
    for name, details in mokedex.items():
        colour = choose_colour(details['type'])
        beast_info = f"name: {name} | element: {details['type']} | special move: {details['move']} | HP: {details['hp']} | MP: {details['mp']}"
        print(change_colour(beast_info, colour))

clear_screen()

mokedex = {}

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
while True:
    name = input("\nInput your beast's name > ")
    type = input("Input your beast's type > ")
    move = input("Input your beast's special move > ")
    hp = input("Input your beast's starting HP > ")
    mp = input("Input your beast's starting MP > ")

    mokedex[name] = {"type": type, "move": move, "hp": hp, "mp": mp}
    
    colour = choose_colour(type)
    print(change_colour(f"Your beast is called {name.capitalize()}. It is a {type.capitalize()} beast with a special move of {move.capitalize()}.", colour))
    
    again = input("\nAgain? y/n > ").lower()
    if again != 'y':
        break

pretty_print(mokedex)