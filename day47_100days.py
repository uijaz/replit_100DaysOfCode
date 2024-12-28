#myGPTexperiment
# using Bing Copilot
# Day 47 - Project Day: Top Trumps

import os
os.system('clear')

# Data for the football players
players = {
    "Vinicius Junior": {"Club": "Real Madrid", "Goals": 25, "Assists": 15, "Appearances": 40, "Pass Accuracy": 85},
    "Mohamed Salah": {"Club": "Liverpool", "Goals": 30, "Assists": 10, "Appearances": 38, "Pass Accuracy": 88},
    "Rodri": {"Club": "Manchester City", "Goals": 10, "Assists": 8, "Appearances": 42, "Pass Accuracy": 92},
    "Erling Haaland": {"Club": "Manchester City", "Goals": 45, "Assists": 5, "Appearances": 40, "Pass Accuracy": 80},
    "Harry Kane": {"Club": "Bayern Munich", "Goals": 35, "Assists": 12, "Appearances": 40, "Pass Accuracy": 87}
}

def prettyPrint(player_name, stats):
    print(f"{player_name}: Club: {stats['Club']}, Goals: {stats['Goals']}, Assists: {stats['Assists']}, Appearances: {stats['Appearances']}, Pass Accuracy: {stats['Pass Accuracy']}")

def get_stat_choice():
    print("Choose your stat:")
    print("1. Goals")
    print("2. Assists")
    print("3. Appearances")
    print("4. Pass Accuracy")
    choice = input("> ")
    return choice

def determine_winner(stat, player1_stat, player2_stat):
    if player1_stat > player2_stat:
        return 1
    elif player1_stat < player2_stat:
        return 2
    else:
        return 0

# Initialize player scores
player1_points = 0
player2_points = 0

print("⚽️Top Football Trumps⚽️")
print("Welcome to the Top Football Trumps Simulator")

# Game loop
while True:
    print()
    print("1 - Vinicius Junior  2 - Mohamed Salah  3 - Rodri  4 - Erling Haaland  5 - Harry Kane")
    
    player1_choice = input("Player1 choose your card > ")
    player2_choice = input("Player2 choose your card > ")
    
    player1_name = list(players.keys())[int(player1_choice) - 1]
    player2_name = list(players.keys())[int(player2_choice) - 1]

    print()
    stat_choice = get_stat_choice()
    
    if stat_choice == "1":
        stat = "Goals"
    elif stat_choice == "2":
        stat = "Assists"
    elif stat_choice == "3":
        stat = "Appearances"
    elif stat_choice == "4":
        stat = "Pass Accuracy"
    else:
        print("Invalid choice!")
        continue

    player1_stat = players[player1_name][stat]
    player2_stat = players[player2_name][stat]

    print()
    print(f"{player1_name} has {stat.lower()} stat of {player1_stat}")
    print(f"{player2_name} has {stat.lower()} stat of {player2_stat}")

    winner = determine_winner(stat, player1_stat, player2_stat)
    if winner == 1:
        print(f"************* {player1_name} wins! ********")
        player1_points += 1
    elif winner == 2:
        print(f"************* {player2_name} wins! ********")
        player2_points += 1
    else:
        print("************* It's a tie! ********")

    # Update and display player scores
    print()
    print(f"Player 1 Points: {player1_points} | Player 2 Points: {player2_points}")

    play_again = input("Play again? y/n > ").lower()
    if play_again != "y":
        break

# Display final scores and the winner
print("\n== Final Scores ==")
print(f"Player 1: {player1_points}")
print(f"Player 2: {player2_points}")

if player1_points > player2_points:
    print("************* Player 1 Wins the Game! *************")
elif player1_points < player2_points:
    print("************* Player 2 Wins the Game! *************")
else:
    print("************* It's a tie! *************")