# Day 42 - Project Day: MokeBeast
import os
from utils_100days import changeColour

os.system('clear')

beast_dict = {}

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