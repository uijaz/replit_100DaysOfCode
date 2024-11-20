# Day 15 - Loops
print("== Cow Sound Generator ==")
exit = "" # Initialize the variable
while exit != "yes":
  animal = input("What animal do you want? ")
  if animal == "cow":
    print("A cow goes moo")
  else:
    print("The" , animal , "goes hurrah!")
  exit = input("'yes' to exit?: ")
  print()
