# Day 43 - 2D Lists
import random, os
os.system('clear')

# pip install tabulate
from tabulate import tabulate

bingo2DList = []
randList = []

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

print("== Bingo Card Generator ==")
print(tabulate(bingo2DList, tablefmt="grid", colalign=('center', 'center', 'center')))