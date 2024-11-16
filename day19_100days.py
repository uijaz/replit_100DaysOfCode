# Day 19 - Let's Be a Bit Lazy!
print("== Loan Calculator ==")
print()

borrowedMoney = float(input("How much money do you want to borrow? "))
apr = float(input("What is the APR%? "))
years = int(input("How many years are you borrowing for? "))
print()

for i in range(years):
  borrowedMoney += borrowedMoney * apr / 100

print(f"You will owe £{round(borrowedMoney, 2)} after {years} years.")
print(f"Your monthly payments will be £{(borrowedMoney / (years * 12)):.2f}.")
