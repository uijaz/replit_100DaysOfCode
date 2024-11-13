# Day 5 - If this...else that?!
print("Which character are you from 'Avengers?'")
print("""Marvel Movie Character Creator
--
(Type Yes or No to answer the questions.)""")
print()

spider = input("Do you like 'hanging around'?: ")
if spider == "Yes":
  print("Hello Spider-man!")
  quit()
else:
  print("You're not Spider-man.")
print()

korg = input("Do you have a 'gravelly' voice?: ")
if korg == "Yes":
  print("Hello Korg!")
  quit()
else:
  print("Aww, you're not Korg.")
print()

captainM = input("Do you often feel 'Marvelous'?: ")
if captainM == "Yes":
  print("Aha! You're Captain Marvel! Hi!")
  quit()
else:
  print("Who are you?")
