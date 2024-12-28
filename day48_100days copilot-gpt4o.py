#myGPTexperiment
# using Copilot with GPT-4o
# Day 48 - Saving Files

# This program should:
# - Ask the user to input their three letter initials and score (out of about 100,000).
# - Save both those values into a file called 'high.score'.
# - This should use append mode. If the file doesn't exist, it should be created. If it does, the score should be added to the end.
# - Each new entry score should go on a new line as initials space score. Then start a new line for the next entry.
# - Add 2-3 scores for testing in a loop.
# - The loop should ask the user if they've finished entering data and stop if they have.
# - Get all the inputs with just one input command and the split function.

# Example Output:
# 🌟HIGH SCORE TABLE🌟
# Input your initials > DJM
# Input your score > 89,764
# Added to high score table.
# Add another? y/n? y
# Input your initials > ACY
# Input your score > 5,731
# Added to high score table.
# Add another? y/n? n

print("🌟HIGH SCORE TABLE🌟")

with open("highscore-copilot.txt", "a+") as f:
    while True:
        user_input = input("Input your initials and score (e.g., DJM 89764) > ")
        initials, score = user_input.split()
        f.write(f"{initials} {score}\n")
        another = input("Add another? y/n? ")
        if another.lower() != 'y':
            break

