# Day 17 - Continue Statement
from getpass import getpass as input

print("== Welcome to Rock🪨, Paper📄, Scissors✂️! ==")

p1 = 0
p2 = 0

while True:
  print("Players, please select your move (r, p or s)")
  
  # player can exit game
  exit = input("Press 'enter' to conitnue or type 'e' to exit: ")
  if exit == "e":
    break

  player1 = input("Player 1: ")
  if player1 != "r" and player1 != "p" and player1 != "s":
    print("Invalid move Player 1!")
    print("=== Reset round ===")
    print()
    continue
  
  player2 = input("Player 2: ")
  if player2 != "r" and player2 != "p" and player2 != "s":
    print("Invalid move Player 2!")
    print("=== Reset round ===")
    print()
    continue
  
  print()
  if player1 == "r" and player2 == "r":
    print("It's a tie!")
  elif player1 == "r" and player2 == "p":
    print("Player 2 wins!")
    p2 += 1
  elif player1 == "r" and player2 == "s":
    print("Player 1 wins!")
    p1 += 1
  elif player1 == "p" and player2 == "r":
    print("Player 1 wins!")
    p1 += 1
  elif player1 == "p" and player2 == "p":
    print("It's a tie!")
  elif player1 == "p" and player2 == "s":
    print("Player 2 wins!")
    p2 += 1
  elif player1 == "s" and player2 == "":
    print("Player 2 wins!")
    p2 += 1
  elif player1 == "s" and player2 == "p":
    print("Player 1 wins!")
    p1 += 1
  elif player1 == "s" and player2 == "s":
    print("It's a tie!")
  else:
    print("Invalid input.")
  print("=== Next round ===")
  print()

# final score
print()
print("Player 1 score:", p1)
print("Player 2 score:", p2)

# match result
if p1 > p2:
  print("Player 1 wins the match!")
elif p1 < p2:
  print("Player 2 wins the match!")
else:
  print("The match is a tie!")
