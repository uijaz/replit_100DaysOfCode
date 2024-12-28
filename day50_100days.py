#myGPTexperiment
# using Copilot with GPT-4o
# Day 50 - Project Day: Idea Storage

# GPT instructions:

# The program for idea storage system should:
# 1. Prompt the user to add an idea, or load a random one.
# 2. Choosing 'Add an idea' results in:
# 2a. A prompt for the user to input their idea.
# 2b. Add the idea to a text file called 'myideas.txt'.
# 2c. Add the idea in append mode, with every new idea on a brand new line.
# 2d. Choosing 'Load random' results in:
# 3. Load the list of ideas.
# 3a. Choose one at random.
# 3b. Display it on screen for a few seconds.
# 3c. Return to the menu.
# - To pick an idea at random, you could use split() to get an array of values. Or you could use random.choice to generate a random number and keep loading lines until you get to the random number line.
# - Try implementing your menu as a subroutine, so you can call it whenever you need to return to it.

# Example output:
# 🌟Idea Storage🌟
# 
# Add an idea or see a random idea? a/r. > r
# 
# Monkey tennis.
# 
# Add an idea or see a ranmdom idea? a/r. > a
# 
# Input your idea. > Youth hostelling with Chris Eubank
# 
# Nice! Your idea has been stored.

# Additional improvements:
# Improve the program to allow for the user to list all ideas, or quit the program.
# Add newlines to the output to make it easier to read.

import random
import time

def menu():
  print("\n🌟Idea Storage🌟")
  choice = input("Add an idea, see a random idea, list all ideas, or quit? a/r/l/q. > ").strip().lower()
  if choice == 'a':
    add_idea()
  elif choice == 'r':
    load_random_idea()
  elif choice == 'l':
    list_all_ideas()
  elif choice == 'q':
    print("Goodbye!")
    exit()
  else:
    print("Invalid choice. Please choose 'a' to add an idea, 'r' to see a random idea, 'l' to list all ideas, or 'q' to quit.")
  menu()

def add_idea():
  idea = input("Input your idea. > ").strip()
  with open('myideas.txt', 'a') as file:
    file.write(idea + '\n')
  print("Nice! Your idea has been stored.")
  menu()

def load_random_idea():
  try:
    with open('myideas.txt', 'r') as file:
      ideas = file.readlines()
    if ideas:
      random_idea = random.choice(ideas).strip()
      print(f"\n{random_idea}\n")
      time.sleep(2)
    else:
      print("No ideas found. Please add some ideas first.")
  except FileNotFoundError:
    print("No ideas found. Please add some ideas first.")
  menu()

def list_all_ideas():
  try:
    with open('myideas.txt', 'r') as file:
      ideas = file.readlines()
    if ideas:
      print("\nAll Ideas:")
      for idea in ideas:
        print(f"- {idea.strip()}")
      print()
    else:
      print("No ideas found. Please add some ideas first.")
  except FileNotFoundError:
    print("No ideas found. Please add some ideas first.")
  menu()

menu()