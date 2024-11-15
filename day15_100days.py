# Day 15 - All About the Loop
print("== Cow Sound Generator ==")
# exit = ""
while exit != "yes":
  animal = input("What animal do you want? ")
  if animal == "cow":
    print("A cow goes moo")
  else:
    print("The" , animal , "goes hurrah!")
  exit = input("'yes' to exit?: ")
  print()
