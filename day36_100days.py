# Day 36 - String Manipulation
names = []

def printList():
  for item in names:
    print(item)

while True:
  fname = input("Enter first name: ").strip().capitalize()
  lname = input("Enter last name: ").strip().capitalize()
  name = f"{fname} {lname}"

  if name not in names:
    names.append(name)
    print()
    printList()
    print()
  else:
    print(f"\n'{name}' already exists.\n")