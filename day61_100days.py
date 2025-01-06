#myGPTexperiment
# using Copilot with GPT-4o
# Day 61: Replit DB

# Spec:
# Display a menu - Add or View tweets, or Exit.
# - Start program by cleaning the console.
# - Use shelve libaray with 'tweets' as the database.
# - 'Add' should:
# -- Get the tweet input.
# -- Store it to the database with the current timestamp as the key value.
# - 'View' should:
# -- Show the tweets in reverse chronological order.
# -- Show 10 tweets at a time.
# -- Prompt the user to show another 10 tweets (yes or no).
# -- A 'no' choice goes back to the menu.
# - 'Exit' should:
# -- Exit the program.
# - Use the datetime library to get the current timestamp.
# - Use Timestamp Code:
# -- timestamp = datetime.datetime.now()
# - Use the os library to clear the console between each 10 tweets shown.

import shelve
import datetime
import os

def add_tweet(db):
  tweet = input("Enter your tweet: ")
  timestamp = datetime.datetime.now().isoformat()
  db[timestamp] = tweet
  print("Tweet added successfully!")

def view_tweets(db):
  keys = sorted(db.keys(), reverse=True)
  for i in range(0, len(keys), 10):
    for key in keys[i:i+10]:
      print(f"{key}: {db[key]}")
    if i + 10 < len(keys):
      more = input("Show more tweets? (yes/no): ")
      if more.lower() != 'yes':
        break

def main():
  os.system('clear')
  with shelve.open('resources/tweets') as db:
    while True:
      print()
      print("Menu:")
      print("1. Add Tweet")
      print("2. View Tweets")
      print("3. Exit")
      choice = input("Enter your choice: ")
      print()
      if choice == '1':
        add_tweet(db)
      elif choice == '2':
        view_tweets(db)
      elif choice == '3':
        break
      else:
        print("Invalid choice. Please try again.")

main()