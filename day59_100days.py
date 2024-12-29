#myGPTexperiment
# using Copilot with GPT-4o
# Day 59: Project Day: Palindrome

# Specs:
# Create a program that checks if a word is a palindrome. A palindrome is a word that reads the same forwards as backwards (ignoring spaces, punctuation, and capitalization). The program should utilize the following concepts:
# - recursion
# - string slicing
# - looping

# Your program should:
# - Prompt the user to input a word.
# - Analyze the word to see if it is a palindrome.
# - Output a relevant 'yes/no message.
# - Ask user if they want to check another word or exit by giving y/n options.

# Example output:
# 🌟Palindrome Checker🌟
# 
# Input a word > Racecar
# Racecar is a palindrome. Yay!

def is_palindrome(word):
  word = ''.join(char.lower() for char in word if char.isalnum())
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  return is_palindrome(word[1:-1])

def main():
  print("🌟Palindrome Checker🌟")
  while True:
    print()
    word = input("Input a word > ")
    if is_palindrome(word):
      print(f"{word} is a palindrome. Yay!")
    else:
      print(f"{word} is not a palindrome.")
    
    again = input("Do you want to check another word? (y/n) > ").lower()
    if again != 'y':
      break

main()