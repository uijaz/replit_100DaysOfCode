# Day 23 - Subroutines
def login():
  print("Replit Login System")
  print()
  uname = input("What is your username?: ")
  pword = input("What is your password? ")
  
  if uname == name and pword == word:
    print("Welcome to Replit!")
    return 1
  else:
    print("Whoops! Username or password do not match. Try again!")
    return 0

name = "david"
word = "pass"

while True:
  print()
  if login():
    break
  else:
    continue
