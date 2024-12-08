# Day 42 - Project Day: MokeBeast
import os
os.system('clear')

beast_dict = {}

# Generates coloured text
def changeColour(text, colour):
    colours_dichangeColour = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    colour_code = colours_dichangeColour.get(colour, colours_dichangeColour["reset"])    
    return f"{colour_code}{text}{colours_dichangeColour['reset']}"

def chooseColour(type):
    if type.lower() == 'fire':
        return 'red'
    elif type.lower() == 'water':
      return 'blue'
    elif type.lower() == 'air':
      return 'white'
    elif type.lower() == 'earth':
      return 'green'
    else:
       return 'yellow'
    

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()
name = input("Input your beast's name > ")
beast_dict.update({"name":name})

type = input("Input your beast's type > ")
beast_dict.update({"type":type})

move = input("Input your beast's special move > ")
beast_dict.update({"move":move})

hp = input("Input your beast's staring HP > ")
beast_dict.update({"hp":hp})

mp = input("Input your beast's staring MP > ")
beast_dict.update({"mp":mp})
print()
colour = beast_dict.get('type')
print(f"{changeColour('Your beast is called ' + name.capitalize() + '. It is an ' + type.capitalize() +  ' beast with a special move of ' + move.capitalize() + '.', chooseColour(colour))}")