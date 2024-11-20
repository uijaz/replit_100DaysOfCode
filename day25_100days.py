# Day 25 - Return Command
def diceRoll(numberOfSides):
    import random
    return random.randint(1, numberOfSides)

def hp():
    return diceRoll(6) * diceRoll(8)

print("== ⚔️ Character Stats Generator ⚔️ ==")
print()

roll = "y"
while roll == "y":
    # change colour to red
    print("\033[31m")
    warrior = input("Name your warrior: ")
    # change colour to green
    print("\033[92m")
    print(f"Their health is: {hp()} hp")
    # revert colour
    print("\033[0m")
    roll = input("Play again (y / n)? ")
    print()
print("Good game!")