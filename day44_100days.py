# Day 44 - 2D Dynamic Lists
import random
import os

# pip install tabulate
from tabulate import tabulate

# Clear the console
os.system('clear')

# Create a 2D list for the bingo card and a list for random numbers
bingo2DList = []
randList = []

def createBingoCard(bingo2DList, randList):
    for i in range(9):
        while True:
            rInt = random.randint(1, 89)
            if rInt not in randList:
                randList.append(rInt)
                break
    sortedList = sorted(randList)

    for i in range(0, 9, 3):
        subList = [sortedList[i], sortedList[i + 1], sortedList[i + 2]]
        bingo2DList.append(subList)
    bingo2DList[1][1] = "BINGO"

def printBingoCard(bingo2DList):
    print("== Bingo Card ==")
    print(tabulate(bingo2DList, tablefmt="grid", colalign=('center', 'center', 'center')))

def checkAndUpdateCard(bingo2DList, number):
    for row in bingo2DList:
        for i in range(len(row)):
            if row[i] == number:
                row[i] = 'X'
                return True
    return False

def isBingo(bingo2DList):
    for row in bingo2DList:
        if any(item != 'X' and item != 'BINGO' for item in row):
            return False
    return True

# Create the bingo card
createBingoCard(bingo2DList, randList)

# Game loop
while True:
    print()
    printBingoCard(bingo2DList)
    number = input("Enter the next number: ")
    
    if number.isdigit():
        number = int(number)
        if checkAndUpdateCard(bingo2DList, number):
            print(f"Number {number} found and marked as 'X'.")
        else:
            print(f"Number {number} is not on the card.")
    else:
        print("Please enter a valid number.")
        continue

    if isBingo(bingo2DList):
        os.system('clear')
        print("Congratulations! You've won Bingo!")
        printBingoCard(bingo2DList)
        break