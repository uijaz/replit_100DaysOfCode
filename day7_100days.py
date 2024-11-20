# Day 7 - Nesting
player = input("Which football star do you like? ")
if player == "ronaldo":
  print("Awesome!")
  number = input("What number shirt does he wear? ")
  if number == "7":
    print("You are a Ronaldo fan!")
  else: 
    print("No joy!")
elif player == "salah":
  print("Awesome!")
  number = input("What number shirt does he wear? ")
  if number == "11":
    print("You are a Salah fan!")
  else:
    print("No joy!")
else:
  print("Are you into football?")
