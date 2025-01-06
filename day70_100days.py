#myGPTexperiment
# using Copilot with GPT-4o
# Day 70: Secrets

# Description: Create a login system for two types of users using environment variables.
"""
Specs:
- Create a login system for two types of users using environment variables.
- Clear screen at start
- Each should have their own username and password set as environment variables.
- At the start check to see if the user and passwords exist in the environment.
- The two types of users:
-- admin - create an envirnment variable called admin_password and ask the user to set the password there. 
-- normal - create an environment variable called normal_password and ask the user to set the password there.
-- If they do not exist, ask the user to set them.
-- Clear the screen
- Ask the user to login.
- The admin user should be greeted with 'Hello root'.
- The normal user should be greeted with 'Hello normie'.
- If the passwords do not match, print 'Invalid password'.
- If the passwords do not exist, print 'Password not set'.
- If the user does not exist, print 'User not found'.
- If the user is not admin or normal, print 'Invalid user'.
- User to press 'enter' to continue.
- Continue the login system until the user is given the option to type 'exit'.
"""

import os
import getpass

def clear_screen():
  os.system('clear')

def set_env_variable(var_name, prompt):
  if not os.getenv(var_name):
    os.environ[var_name] = getpass.getpass(prompt)

def login():
  clear_screen()
  set_env_variable('admin_password', 'Set admin password: ')
  set_env_variable('normal_password', 'Set normal password: ')

  while True:
    clear_screen()
    user_type = input("Enter user type (admin/normal) or 'exit' to quit: ").strip().lower()
    if user_type == 'exit':
      break

    if user_type not in ['admin', 'normal']:
      print("Invalid user")
      input("Press 'enter' to continue...")
      continue

    password = getpass.getpass("Enter password: ")
    env_password = os.getenv(f'{user_type}_password')

    if env_password is None:
      print("Password not set")
    elif password == env_password:
      if user_type == 'admin':
        print("Hello root")
      else:
        print("Hello normie")
    else:
      print("Invalid password")

    input("Press 'enter' to continue...")

clear_screen()
print("🌟Login System🌟")
input("Press 'enter' to continue...")
login()