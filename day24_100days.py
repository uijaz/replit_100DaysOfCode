# Day 24 - Parameters
print("== Infinity Dice 🎲 ==")
print()

def diceRoll(numberOfSides):
    import random
    return random.randint(1, numberOfSides)

roll = "y"
while roll == "y":
    sides = int(input("How many sides?: "))
    print("You rolled: ", diceRoll(sides))
    print()
    roll = input("Roll again (y / n)? ")
    print()

print("Good game!")