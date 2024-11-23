# Day 28 - Project Day: Epic Character Battle, Part 2
# Automated game battle system!
import os, time, random
os.system("clear")

# Roll of dice
def diceRoll(numberOfSides):
  return random.randint(1, numberOfSides)

# Character Builder
def character():
  name = input("Name Your Legend: ")
  type = input("Character Type (Human, Elf, Wiard, Orc): ")

  ctype = ""
  if type == "Human" or type =="human":
      ctype = "Adaptable"
  elif type == "Elf" or type == "elf":
      ctype = "Agile"
  elif type == "Wizard" or type == "wizard":
      ctype = "Spellbinding"
  elif type == "Orc" or type == "orc":
      ctype = "Strong"
  else:
      ctype = "Invisible"

  return {
          "name": name + " the " + ctype, # Name
          "strength": characterHealth(),  # Strength
          "health": characterStrength()}  # Health

# Display character specs
def playerSpecs(player):
  print(f"""
          {player["name"]}
          Health: {player["health"]}
          Strength: {player["strength"]}""")

# Generate character's health stats
def characterHealth():
    return int(((diceRoll(6) * diceRoll(12)) / 2) + 10)

# Generate character's strength stats
def characterStrength():
    return int(((diceRoll(6) * diceRoll(12)) / 2) + 12)

# Difference of strength of both opponents and + 1
def damage (player1, player2):
  return abs(player1["strength"] - player2["strength"]) + 1

# Display countdown to round
def countdown(rounds):
    print("-- Round", rounds, " --")
    print()
    time.sleep(1)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("Flight!")
    print()
    time.sleep(1)

# Battle simulator
def battleEngine(player1, player2):
  dice = 6
  rounds = 0
  print("⚔️ BATTLE TIME ⚔️")
  print()
  time.sleep(3)
  os.system("clear")
  while True:
    rounds = rounds + 1
    #  if player health is above 0
    if player1["health"] > 0 and player2["health"] > 0:

      print(player1["name"], "- health:", player1["health"])
      print(player2["name"], "- health:", player2["health"])
      print()
      time.sleep(1)

      countdown(rounds)

      player1_roll = diceRoll(dice)
      player2_roll = diceRoll(dice)
      
      # player1 wins round
      if player1_roll > player2_roll:
        # player2 health is decreased
        damage1 = damage(player1, player2)
        player2["health"] = player2["health"] - damage1
        # change colour to red
        print("\033[31m", player2["name"], "takes a hit with", damage1, "damage.")
        # change colour to green
        print("\033[32m", player1["name"], "wins the round!")
        # revert colour
        print("\033[0m")

      # player 2 wins round
      elif player1_roll < player2_roll:
        # player1 health is decreased
        damage2 = damage(player1, player2)
        player1["health"] = player1["health"] - damage2
        # change colour to red
        print("\033[31m", player1["name"], "takes a hit with", damage2, "damage.")
        # change colour to green
        print("\033[32m", player2["name"], "wins the round!")
        # revert colour
        print("\033[0m")

      # players draw the round
      else:
        # player 1 and player2 health is decreased by 1
        player1["health"] = player1["health"] - 1
        player2["health"] = player2["health"] - 1
        print("\033[33m It is a draw!")
        print("\033[0m")

      time.sleep(3)

    # results
    else:
      if player1["health"] > 0:
        print(player2["name"], "died!")
        print(player1["name"], "won after", rounds, "rounds!")
        print()
      elif player2["health"] > 0:
        print(player1["name"], "died!")
        print(player2["name"], "won after", rounds, "rounds!")
        print()
      break

# Simulate batter between two different characters 
def play():
  print("== Automated Battle System! ==")
  time.sleep(2)
  os.system("clear")
  
  number_of_players = 2
  play = "y"

  while True:
    if play == "Y" or play == "y":

      player1 = character()
      print()
      print("Who are they battling?")
      print()
      player2 = character()
      print()
      time.sleep(2)
      os.system("clear")

      # Display player specs
      print("Legends ready!")
      print()
      playerSpecs(player1)
      print()
      print("Versus..")
      playerSpecs(player2)
      print()
      time.sleep(3)
      os.system("clear")

      battleEngine(player1, player2)

      # Play again?
      play = input("Would you like to have another go (Y / N)? ")
      os.system("clear")
    else:
      print("Good game!")
      print()
      break

play()