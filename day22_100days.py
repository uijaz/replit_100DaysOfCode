# Day 22 - Libraries
import random

print("=== Totally Random One-Million-to-One ===")

# Generate a random integer
random_int = random.randint(1, 1000000)
counter = 1

while True:
  guess = int(input("Guess the number between 1 and 1,000,000: "))
  if guess < random_int:
    print("Too low")
    counter += 1
  elif guess > random_int:
    print("Too high")
    counter += 1
  else:
    print("Correct!")
    print("You guessed it in", counter, "attempts!")
    playAgain = input("Play again (y / n)? ")
    if playAgain == "y":
      continue
    else:
      break
