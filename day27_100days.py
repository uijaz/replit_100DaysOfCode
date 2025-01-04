# Day 27 - Project Day: Epic Character Battle, Part 1
# Character Builder
import os, time, random
from utils_100days import diceRoll

os.system("clear")
print("== Character Builder ==")
time.sleep(1)

# Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
def character(name, type):
    ctype = ""
    if type == "Human" or type =="human":
       ctype = "Adaptable"
    elif type == "Elf" or type == "elf":
       ctype = "Agile"
    elif type == "Wizard" or type == "wizard":
       ctype = "Spellbinding"
    elif type == "Orc" or type == "orc":
       ctype = "Strong"
    else:
       ctype = "Invisible"
    return f"""
                Hello {name} the {ctype}
                Health: {characterHealth()}
                Strength: {characterStrength()}"""


# Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:
def characterHealth():
    return (((diceRoll(6) * diceRoll(12)) / 2) + 10)

# Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's strength stats. Use this formula:
def characterStrength():
    return (((diceRoll(6) * diceRoll(12)) / 2) + 12)

# Present the data in a menu with time.sleep and os.system("clear") to make it appealing.
def menu():
  os.system("clear")
  name = input("Name Your Legend: ")
  print()
  type = input("Character Type (Human, Elf, Wiard, Orc): ")
  time.sleep(1)
  print(character(name, type))
  print()
  print("May your name go down in Legend..")
  print()

# Wrap it in a loop so the user has the option to create another character.
play = "y"
while True:
  if play == "Y" or play == "y":
    menu()
    play = input("Would you like to have another go (Y / N)? ")
    print()
    continue
  else:
    print("Good game!")
    print()
    break