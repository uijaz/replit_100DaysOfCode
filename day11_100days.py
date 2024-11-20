# Day 11 - Project Day! How many seconds in a year
print("== How many seconds are in a year? ==")
yearType = input("Is it a leap year? (y/n) ")

if yearType == "y":
  # 31622400 seconds
  seconds = 60 * 60 * 24 * 366
  print("There are", seconds, "seconds in a leap year.")
elif yearType == "n":
  # 31536000 seconds
  seconds = 60 * 60 * 24 * 365
  print("There are", seconds, "seconds in a year.")
else:
  print("Invalid input.")
