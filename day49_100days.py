#myGPTexperiment
# using Copilot with GPT-4o
# Day 49 - Reading a File

# GPT instructions:

# The program should:
# - Read in the data from the highscore.txt file.
# - Identify which of those users had the highest score. Automatically!
# - Output the name and score of the winner.
# - Read each element one at a time.
# - Split each element into two pieces.
# - You'll have to cast one element as an integer to make it a number.
# - Think back to list indexing to access the second index for the score.
# - Use a max_score list to store the details of the high scorer (starting with line 1 from the file, overwrite the details if the current line has a higher score).

# Example output:
# 🌟Current Leader🌟
# 
# Analyzing high scores......
# 
# Current leader is DJM 898,000

print("🌟Current Leader🌟\n")
print("Analyzing high scores......\n")

with open("highscore.txt", "r") as file:
  max_score = ["", 0]  # [name, score]
  for line in file:
    name, score = line.split()
    score = int(score.replace(",", ""))
    if score > max_score[1]:
      max_score = [name, score]

print(f"Current leader is {max_score[0]} {max_score[1]:,}")