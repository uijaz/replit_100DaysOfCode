#myGPTexperiment
# using Qwen2.5-coder:latest
# Day 48 - Saving Files

# Create python program to:
# - Ask the user to input their three letter initials and score (out of about 100,000).
# - Save both those values into a file called 'high.score.txt'.
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

def add_high_score():
    while True:
        # Ask for user input
        user_input = input("Input your initials and score (e.g., DJM 89,764) > ").strip()
        
        if not user_input:
            print("Invalid input. Please try again.")
            continue
        
        # Split the input into initials and score
        parts = user_input.split()
        if len(parts) != 2 or not parts[0].isalpha() or not parts[1].isdigit():
            print("Invalid format. Please enter initials followed by a space and then a score.")
            continue
        
        initials, score = parts
        
        # Convert score to integer
        try:
            score = int(score)
        except ValueError:
            print("Score must be a number. Please try again.")
            continue
        
        # Append the score to the file
        with open('highscore-qwen.txt', 'a') as file:
            file.write(f"{initials} {score}\n")
        
        print("Added to high score table.")
        
        # Ask if user wants to add another entry
        another = input("Add another? y/n? ").strip().lower()
        if another != 'y':
            break

print("\n🌟HIGH SCORE TABLE🌟")

# Call the function to start adding scores
add_high_score()