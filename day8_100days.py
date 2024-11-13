# Day 8 - Affirmation Generator
name = input("What is your name? ")
day = input("What day is it today? ")
fav1 = input("Name one of your favorite things? ")
fav2 = input("Name another thing? ")
fav3 = input("And another? ")

if day == "Monday" or day == "monday":
  unique = "fun"
if day == "Tuesday" or day == "tuesday":
  unique = "good"
if day == "Wednesday" or day == "wednesday":
  unique = "great"
if day == "Thursday" or day == "thursday":
  unique = "wonderful"
if day == "Friday" or day == "friday":
  unique = "fantastic"
if day == "Saturday" or day == "saturday":
  unique = "slow"
if day == "Sunday" or day == "sunday":
  unique = "lazy"

message = f"Hey {name}, great to see you today! I hope you have a {unique} {day} and that you get some {fav1}, {fav2} and {fav3}."
print(message)
