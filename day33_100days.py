# Day 33 - Dynamic Lists
import os
os.system("clear")

def printList(list):
  print()
  for item in list:
    print(f"\033[32m{item}\033[0m")   # green
  print() 

list = []
print("\033[33m== To Do List Manager ==\033[0m")
print()

while True:
  action = input("Would you like to view, add or remove you To Do list? ")
  if action == "view" or action == "View":
    printList(list)
  elif action == "add" or action == "Add":
    item = input("Add item to your To Do list: ")
    print()
    list.append(item)
  elif action == "remove" or action == "Remove":
    item = input("Which item have you completed: ")
    print()
    if item in list:
      list.remove(item)
    else:
      print(f"\033[31m{item} was not in your To Do list.\033[0m")   #red
      print()