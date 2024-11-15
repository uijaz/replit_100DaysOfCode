# Day 16 - Make it Stop!
print("== Guess this song! ==")
print()
print("Fill in the blank ____!")
counter = 1

while True:
  print()
  print("Never going to ____ you up.")
  word = input("What is the missing word? ")
  if word == "give":
    print()
    break
  print("Try again!")
  counter += 1
print("Well done! It only took you", counter, "attempts.")
