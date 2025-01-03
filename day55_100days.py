#myGPTexperiment
# using Copilot with GPT-4o
# Day 55: Os Library

# Improve Day 51: Saving and Loading Data

# Specs:
# Improve existing code by:
# Create a backup folder. Use the 'os.mkdir()' function.
# Create a random filename to create a backup file. Save a copy of the data to this file.
# This backup saving should all happen before the auto save.
# Use a Boolean variable 'fileExists' set to False to store whether the random filename file has already been created.
# Use 'if fileExists' later on to check the status of the file before creating or writing.
# Make sure all data is backed up in this new file along with the todo.txt.

import os, time, ast, random, string
from utils_100days import changeColour

os.system("clear")

todo_list = []
fileExists = False

def createBackupFolder():
    if not os.path.exists("backup"):
        os.mkdir("backup")

def generateRandomFilename():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".txt"

def saveBackup():
    global fileExists
    createBackupFolder()
    backup_filename = generateRandomFilename()
    backup_filepath = os.path.join("backup", backup_filename)
    while os.path.exists(backup_filepath):
        backup_filename = generateRandomFilename()
        backup_filepath = os.path.join("backup", backup_filename)
    with open(backup_filepath, "w") as f:
        f.write(str(todo_list))
    fileExists = True

def saveList():
    saveBackup()
    with open("todo.txt", "w") as f:
        f.write(str(todo_list))

def loadList():
    global todo_list
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as f:
            todo_list = ast.literal_eval(f.read())

def viewList():
    if len(todo_list) == 0:
        print(changeColour("Your To Do list is currently empty.", "yellow"))
    else:
        print(changeColour("Here is your To Do list:", "green"))
        for idx, task in enumerate(todo_list):
            print(changeColour(f"{idx + 1}. {task['task']} - Due: {task['due']} - Priority: {task['priority']}", "cyan"))

def viewByPriority(priority):
    filtered_tasks = [task for task in todo_list if task['priority'] == priority]
    if not filtered_tasks:
        print(changeColour(f"No tasks with {priority} priority.", "yellow"))
    else:
        print(changeColour(f"{priority.capitalize()} priority tasks:", "green"))
        for idx, task in enumerate(filtered_tasks):
            print(changeColour(f"{idx + 1}. {task['task']} - Due: {task['due']}", "cyan"))

def addItem():
    task = input(changeColour("What is the task? ", "yellow"))
    due = input(changeColour("When is it due? ", "yellow"))
    priority = input(changeColour("What is the priority (high, medium, low)? ", "yellow")).lower()

    if priority not in ["high", "medium", "low"]:
        print(changeColour("Invalid priority! Task not added.", "red"))
        return

    new_task = {"task": task, "due": due, "priority": priority}

    if priority == "high":
        todo_list.insert(0, new_task)
    elif priority == "medium":
        mid_index = len([t for t in todo_list if t['priority'] == "high"])
        todo_list.insert(mid_index, new_task)
    else:
        todo_list.append(new_task)

    print(changeColour("Task added successfully!", "green"))
    saveList()

def editItem():
    if not todo_list:
        print(changeColour("Your To Do list is empty.", "yellow"))
        return

    viewList()
    task_num = input(changeColour("Enter the task number to edit: ", "yellow"))

    if not task_num.isdigit():
        print(changeColour("Invalid input!", "red"))
        return

    task_num = int(task_num) - 1

    if task_num < 0 or task_num >= len(todo_list):
        print(changeColour("Invalid task number!", "red"))
        return

    print(changeColour("Leave fields blank to keep existing values.", "blue"))
    task = input(changeColour("New task name: ", "yellow")) or todo_list[task_num]['task']
    due = input(changeColour("New due date: ", "yellow")) or todo_list[task_num]['due']
    priority = input(changeColour("New priority (high, medium, low): ", "yellow")).lower() or todo_list[task_num]['priority']

    if priority not in ["high", "medium", "low"]:
        print(changeColour("Invalid priority! Task not edited.", "red"))
        return

    todo_list.pop(task_num)
    new_task = {"task": task, "due": due, "priority": priority}
    if priority == "high":
        todo_list.insert(0, new_task)
    elif priority == "medium":
        mid_index = len([t for t in todo_list if t['priority'] == "high"])
        todo_list.insert(mid_index, new_task)
    else:
        todo_list.append(new_task)

    print(changeColour("Task edited successfully!", "green"))
    saveList()

def removeItem():
    if not todo_list:
        print(changeColour("Your To Do list is empty.", "yellow"))
        return

    viewList()
    task_num = input(changeColour("Enter the task number to remove: ", "yellow"))

    if not task_num.isdigit():
        print(changeColour("Invalid input!", "red"))
        return

    task_num = int(task_num) - 1

    if task_num < 0 or task_num >= len(todo_list):
        print(changeColour("Invalid task number!", "red"))
        return

    removed_task = todo_list.pop(task_num)
    print(changeColour(f"Task '{removed_task['task']}' removed successfully!", "green"))
    saveList()

def deleteList():
    if not todo_list:
        print(changeColour("Your To Do list is empty.", "yellow"))
        return

    confirm = input(changeColour("Are you sure you want to delete the entire list? (y/n): ", "red")).lower()
    if confirm == "y":
        todo_list.clear()
        print(changeColour("Your To Do list has been deleted.", "red"))
    else:
        print(changeColour("Your To Do list was not deleted.", "green"))
    saveList()

def moveItem():
    if not todo_list:
        print(changeColour("Your To Do list is empty.", "yellow"))
        return

    viewList()
    task_num = input(changeColour("Enter the task number to move: ", "yellow"))

    if not task_num.isdigit():
        print(changeColour("Invalid input!", "red"))
        return

    task_num = int(task_num) - 1

    if task_num < 0 or task_num >= len(todo_list):
        print(changeColour("Invalid task number!", "red"))
        return

    new_priority = input(changeColour("Enter the new priority (high, medium, low): ", "yellow")).lower()
    if new_priority not in ["high", "medium", "low"]:
        print(changeColour("Invalid priority! Task not moved.", "red"))
        return

    task = todo_list.pop(task_num)
    task['priority'] = new_priority

    if new_priority == "high":
        todo_list.insert(0, task)
    elif new_priority == "medium":
        mid_index = len([t for t in todo_list if t['priority'] == "high"])
        todo_list.insert(mid_index, task)
    else:
        todo_list.append(task)

    print(changeColour("Task moved successfully!", "green"))
    saveList()

def todoMenu():
    loadList()
    while True:
        print()
        action = input(changeColour("Do you want to view, add, edit, remove, move, delete the list, or exit? ", "yellow")).lower()
        print()
        if action == "view":
            sub_action = input(changeColour("View all or by priority? (all/priority): ", "yellow")).lower()
            if sub_action == "all":
                viewList()
            elif sub_action == "priority":
                priority = input(changeColour("Enter priority (high, medium, low): ", "yellow")).lower()
                viewByPriority(priority)
            else:
                print(changeColour("Invalid option!", "red"))
        elif action == "add":
            addItem()
        elif action == "edit":
            editItem()
        elif action == "remove":
            removeItem()
        elif action == "move":
            moveItem()
        elif action == "delete":
            deleteList()
        elif action == "exit":
            print(changeColour("Exiting...", "red"))
            time.sleep(1)
            os.system("clear")
            exit()
        else:
            print(changeColour("Invalid input!", "red"))

print(changeColour("== To Do List Manager ==", "yellow"))
todoMenu()