# Day 35 - ProjechangeColour Day: The ULTIMATE List Maker
import os, time
os.system("clear")

list = []
index = 0

item = ""
new_item = ""
ans = ""

# Generates coloured text
def changeColour(text, colour):
    colours_dichangeColour = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    colour_code = colours_dichangeColour.get(colour, colours_dichangeColour["reset"])    
    return f"{colour_code}{text}{colours_dichangeColour['reset']}"
  
def viewList(list):
  if len(list) == 0:
    print(f"{changeColour('Your To Do list is currently empty.', 'yellow')}")
    return 0
  else:
    print(f"{changeColour('Here is your To Do list:', 'green')}")
    for item in list:
      print(f"{changeColour(item, 'green')}")
  
def addItem(list):
    item = input(f"{changeColour('What item do you want to add? ', 'yellow')}")
    if item in list:
      print(f"{changeColour(item + ' already exists, duplicates are not allowed.', 'red')}")
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
        new_item = input(f"{changeColour('Add new item: ', 'yellow')}")
        index = list.index(item)
        list[index] = new_item
      else:
        print(f"{changeColour(item + ' does not exist.', 'red')}")

def removeItem(list):
    if viewList(list) == 0:
      pass
    else:
      print()
      item = input("What item do you want to remove? ")
      if item in list:
        ans = input(f"{changeColour('Are you sure (y / n)? ', 'yellow')}")
        print()
        if ans == "y" or ans == "Y":
          list.remove(item)
          print(f"{changeColour(item + ' was removed from your To Do list.', 'red')}")
        else:
          print(f"{changeColour(item + ' was not removed from your To Do list.', 'red')}")
      else:
        print(f"{changeColour(item + ' was not in your To Do list.', 'red')}")

def deleteList(list):
    if viewList(list) == 0:
      pass
    else:
      print()
      ans = input(f"{changeColour('Are you sure (y / n)? ', 'yellow')}")
      if ans == "y" or ans == "Y":
        ans = input(f"{changeColour('Your To Do list will be deleted forever, are you sure (y / n)? ', 'red')}")
        if ans == "y" or ans == "Y":
          list.clear()
          print(f"{changeColour('Your To Do list was deleted.', 'red')}")
        else:
            print(f"{changeColour('Your To Do list was not deleted.', 'green')}")
      else:
          print()
          print(f"{changeColour('Your To Do list was not deleted.', 'green')}")

def todoMenu():
    while True:
      achangeColourion = input(f"Do you want to view, add, edit, remove or delete the To Do list? (or exit) ")
      print()
      if achangeColourion == "view" or achangeColourion == "View":
        viewList(list)
        print()
      elif achangeColourion == "add" or achangeColourion == "Add":
        addItem(list)
        print()
      elif achangeColourion == "edit" or achangeColourion =="Edit":
        editItem(list)
        print()
      elif achangeColourion == "remove" or achangeColourion == "Remove":
        removeItem(list)
        print()
      elif achangeColourion == "exit" or achangeColourion == "Exit":
        print(f"{changeColour('Exiting .. ', 'red')}")
        time.sleep(1)
        os.system("clear")
        exit()
      elif achangeColourion == 'delete' or achangeColourion =='Delete':
        deleteList(list)
        print()
      else:
        print(f"{changeColour(item + 'Invalid input!', 'red')}")   #red
        print()

print(f"{changeColour('== To Do List Manager ==', 'yellow')}")
print()
todoMenu()