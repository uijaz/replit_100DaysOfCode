# Day 18 - Guess the Number
import random

print("=== Guess the Number ===")

# Generate a random integer
random_int = random.randint(1, 5)
counter = 1

while True:
  guess = int(input("Guess the number between 1 and 5: "))
  if guess < random_int:
    print("Too low")
    counter += 1
  elif guess > random_int:
    print("Too high")
    counter += 1
  else:
    print("You guessed it in", counter, "attempts!")
    break
