# Day 10 - A bit of Math
myBill = float(input("What was the bill?: "))
tip = int(input("What percentage of tip would you like to leave? "))
totalBill = myBill + (myBill * (tip / 100))
numberOfPeople = int(input("How many people?: "))
answer = totalBill / numberOfPeople
answerTwoDec = round(answer, 2)
print("You all owe", answerTwoDec)
