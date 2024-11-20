# Day 21 - Project Day! Build a Math Facts Game
print("== Math Game! ==")

while True:
  multiplicand = int(input("Name your multiplicand: "))
  print()
  score = 0
  for i in range(1, 11):
    answer = int(input(f"{i} x {multiplicand} = "))
    if answer == i * multiplicand:
      print("Great work!")
      score += 1
    else:
      print("No joy! The answer was", i * multiplicand)
  print()
  print(f"You scored {score} out of {i}.")
  tryAgain = input("Would you like to try again (y / n)? ")
  print("---")
  if tryAgain != "y" and tryAgain != "Y":
    break
print("Keep practicing!")
