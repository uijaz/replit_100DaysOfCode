#myGPTexperiment
# using Copilot with GPT-4o
# Day 62: Project Day: Private Diary

# Specs:
# A private diary to keep secret thoughts.
# Your diary should:
# - Set an access password.
# - Prompt the user to type in a password.
# - If they don't get the password right, exit the program.
# - If they get it right, they enter the main menu, which gives 'Add' or 'View' diary entries.
# - Choosing 'add' should:
# -- Prompt the user to type the entry and store it in the database with the timestamp as the key.
# - Choosing 'view' should:
# -- Show the user the previous (most recent) entry.
# - They can then choose to see the next previous entry working backwards until they get to the end. Or exit back to the menu.
# - Use shelve library for the database.
# - Add a feature which allows the user to view an entry from an exact date.
# - Use if passwordEntered != correctPassword to verify the user.
# - Use os.clear() to clear the screen between each entry viewed.
# - Compare the date entered to the timestamp and only show if date entered >= timestamp.

import shelve
import os
from datetime import datetime

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def set_password():
  with shelve.open('diary') as db:
    if 'password' not in db:
      password = input("Set your diary password: ")
      db['password'] = password

def verify_password():
  with shelve.open('diary') as db:
    correct_password = db['password']
    password_entered = input("Enter your diary password: ")
    if password_entered != correct_password:
      print("Incorrect password. Exiting...")
      exit()

def add_entry():
  with shelve.open('diary') as db:
    entry = input("Type your entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db[timestamp] = entry
    print("Entry added.")

def view_entries():
  with shelve.open('diary') as db:
    keys = sorted(db.keys(), reverse=True)
    keys = [key for key in keys if key != 'password']
    index = 0
    while True:
      if index < len(keys):
        clear_screen()
        print(f"Entry from {keys[index]}:\n{db[keys[index]]}")
        action = input("Enter 'n' for next, 'p' for previous, 'e' to exit: ").lower()
        if action == 'n':
          index += 1
        elif action == 'p' and index > 0:
          index -= 1
        elif action == 'e':
          break
        else:
          print("Invalid input.")
      else:
        print("No more entries.")
        break

def view_entry_by_date():
  date_str = input("Enter the date (YYYY-MM-DD): ")
  with shelve.open('diary') as db:
    keys = sorted(db.keys())
    keys = [key for key in keys if key != 'password']
    entries_found = False
    clear_screen()
    for key in keys:
      if key.startswith(date_str):
        print(f"Entry from {key}:\n{db[key]}\n{'-'*40}")
        entries_found = True
    if not entries_found:
      print("No entries found for the given date.")
    input("Press Enter to return to the menu.")

def view_all_entries():
  with shelve.open('diary') as db:
    keys = sorted(db.keys())
    keys = [key for key in keys if key != 'password']
    clear_screen()
    for key in keys:
      print(f"Entry from {key}:\n{db[key]}\n{'-'*40}")
    input("Press Enter to return to the menu.")

def main_menu():
  while True:
    clear_screen()
    print("Diary Menu:")
    print("1. Add entry")
    print("2. View entries")
    print("3. View entry by date")
    print("4. View all entries")
    print("5. Exit")
    choice = input("Choose an option: ")
    print()
    if choice == '1':
      add_entry()
    elif choice == '2':
      view_entries()
    elif choice == '3':
      view_entry_by_date()
    elif choice == '4':
      view_all_entries()
    elif choice == '5':
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  clear_screen()
  set_password()
  verify_password()
  main_menu()