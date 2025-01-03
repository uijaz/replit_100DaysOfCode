from utils_100days import diceRoll

# Day 24 - Parameters
print("== Infinity Dice 🎲 ==")
print()

roll = "y"
while roll == "y":
    sides = int(input("How many sides?: "))
    print("You rolled: ", diceRoll(sides))
    print()
    roll = input("Roll again (y / n)? ")
    print()

print("Good game!")