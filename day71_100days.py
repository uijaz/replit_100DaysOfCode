#myGPTexperiment
# using Copilot with GPT-4o
# Day 71: Pass the Salt

# Description: Create a simple login system.
"""
### Specs ###
- Create a simple login system with shelve library.
- Display a menu with the ability to add a user or login.
- 'Add' user is a function which should:
-- Ask for a username and password.
-- Create a new password and a randomly generated a 4 digit salt.
-- Append the salt to the password and then hash it.
-- Store the hash and the salt in a shelve dictionary with the username as the key.
- 'Login' is a function which should:
-- Ask for a username and password input.
-- Display a success message if details are correct.
- This system should work with multiple users.

### Example output ###
🌟Login System🌟

1: Add User, 2: Login >  1

Username: > Kenny
Password: > L0gg1ns

Details stored.

1: Add User, 2: Login >  2

Username: > Kenny
Password: > L0gg1ns

Login successful
"""

import shelve
import hashlib
import os

def hash_password(password, salt):
  return hashlib.sha256((password + salt).encode()).hexdigest()

def add_user():
  username = input("Username: > ")
  password = input("Password: > ")
  salt = os.urandom(4).hex()
  hashed_password = hash_password(password, salt)
  
  with shelve.open('resources/login_system') as db:
    db[username] = {'salt': salt, 'password': hashed_password}
  
  print("Details stored.")

def login():
  username = input("Username: > ")
  password = input("Password: > ")
  
  with shelve.open('resources/login_system') as db:
    if username in db:
      salt = db[username]['salt']
      hashed_password = hash_password(password, salt)
      if hashed_password == db[username]['password']:
        print("Login successful")
      else:
        print("Incorrect password")
    else:
      print("Username not found")

def main():
  while True:
    print("\n🌟Login System🌟")
    choice = input("1: Add User, 2: Login > ")
    
    if choice == '1':
      add_user()
    elif choice == '2':
      login()
    else:
      print("Invalid choice")

main()