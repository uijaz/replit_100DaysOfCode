# Day 14 - Rock, Paper, Scissors
from getpass import getpass as input

print("== Welcome to Rock🪨, Paper📄, Scissors✂️! ==")
print()
print("Players, please select your move (r, p or s)")
player1 = input("Player 1: ")
if player1 != "r" and player1 != "p" and player1 != "s":
  print("Invalid move Player 1!")
  quit()

player2 = input("Player 2: ")
if player2 != "r" and player2 != "p" and player2 != "s":
  print("Invalid move Player 2!")
  quit()

print()
if player1 == "r" and player2 == "r":
  print("It's a tie!")
elif player1 == "r" and player2 == "p":
  print("Player 2 wins!")
elif player1 == "r" and player2 == "s":
  print("Player 1 wins!")
elif player1 == "p" and player2 == "r":
  print("Player 1 wins!")
elif player1 == "p" and player2 == "p":
  print("It's a tie!")
elif player1 == "p" and player2 == "s":
  print("Player 2 wins!")
elif player1 == "s" and player2 == "":
  print("Player 2 wins!")
elif player1 == "s" and player2 == "p":
  print("Player 1 wins!")
elif player1 == "s" and player2 == "s":
  print("It's a tie!")
else:
  print("Invalid input.")
