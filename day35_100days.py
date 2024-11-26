# Give the user the option to completely erase the to do list. (You should be able to do this in one line of code!)
import os, time
os.system("clear")

list = []
index = 0

red = "\033[31m"
green = "\032[33m"
yellow = "\033[33m"
reset_colour = "\033[0m"

item = ""
new_item = ""
ans = ""

print(f"{yellow}== To Do List Manager =={reset_colour}")
print()

# Generates coloured text
def cT(text, colour):
    # Dictionary of ANSI escape codes for different colors
    colours_dict = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    colour_code = colours_dict.get(colour, colours_dict["reset"])    
    return f"{colour_code}{text}{colours_dict['reset']}"

def itemInList(item, list):
  if item in list:
    return True
  else:
    return False
  
def viewList(list):
  if len(list) == 0:
    print(f"{cT('Your To Do list is currently empty.', 'yellow')}")
    return 0
  else:
    print(f"{cT('Here is your To Do list:', 'green')}")
    for item in list:
      print(f"{cT(item, 'green')}")
  
def addItem(list):
    item = input(f"{cT('What item do you want to add? ', 'yellow')}")
    if item in list:
      print(f"{cT(item + ' already exists, duplicates are not allowed.', 'red')}")
    else:
      list.append(item)

def editItem(list):
    if viewList(list) == 0:
      pass
    else:
      print()
      item = input(f"What item do you want to edit? ")
      print()
      if item in list:
        new_item = input(f"{cT('Add new item: ', 'yellow')}")
        index = list.index(item)
        list[index] = new_item
      else:
        print(f"{cT(item + ' does not exist.', 'red')}")

def removeItem(list):
    if viewList(list) == 0:
      pass
    else:
      print()
      item = input("What item do you want to remove? ")
      if item in list:
        ans = input(f"{cT('Are you sure (y / n)? ', 'yellow')}")
        print()
        if ans == "y" or ans == "Y":
          list.remove(item)
          print(f"{cT(item + ' was removed from your To Do list.', 'red')}")
        else:
          print(f"{cT(item + ' was not removed from your To Do list.', 'red')}")
      else:
        print(f"{cT(item + ' was not in your To Do list.', 'red')}")

def deleteList(list):
    if viewList(list) == 0:
      pass
    else:
      print()
      ans = input(f"{cT('Are you sure (y / n)? ', 'yellow')}")
      if ans == "y" or ans == "Y":
        ans = input(f"{cT('Your To Do list will be deleted forever, are you sure (y / n)? ', 'red')}")
        if ans == "y" or ans == "Y":
          list.clear()
          print(f"{cT('Your To Do list was deleted.', 'red')}")
        else:
            print(f"{cT('Your To Do list was not deleted.', 'green')}")
      else:
          print()
          print(f"{cT('Your To Do list was not deleted.', 'green')}")

def todoMenu():
    while True:
      action = input(f"Do you want to view, add, edit, remove or delete the To Do list? (or exit) ")
      print()
      if action == "view" or action == "View":
        viewList(list)
        print()
      elif action == "add" or action == "Add":
        addItem(list)
        print()
      elif action == "edit" or action =="Edit":
        editItem(list)
        print()
      elif action == "remove" or action == "Remove":
        removeItem(list)
        print()
      elif action == "exit" or action == "Exit":
        print(f"{cT('Exiting .. ', 'red')}")
        time.sleep(1)
        os.system("clear")
        exit()
      elif action == 'delete' or action =='Delete':
        deleteList(list)
        print()
      else:
        print(f"{cT(item + 'Invalid input!', 'red')}")   #red
        print()

todoMenu()