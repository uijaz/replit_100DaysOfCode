#myGPTexperiment
# using Copilot with GPT-4o
# Day 52: Saving and Loading Data

# Specs:
# Video game inventory system.
# - Have a menu that allows the user to:
# -- Add
# -- View
# -- Remove
# - Adding an item saves it to a file using captalize mode. Duplicates are allowed.
# - Removing an item deletes it from the file.
# - View should output the name of the item and tell you how many of those items you have.
# - Use auto-save and auto-load with try... except.

# Example output with new lines:
# 🌟RPG Inventory🌟
# 1: Add  2: Remove  3: View  > 1
# 
# Input the item to add: > Mana potion
# Mana potion has been added to your inventory.
# 
# 1: Add  2: Remove  3: View  > 2
# 
# Input the item to remove: > Sword
# Sword has been removed from your inventory.
# 
# 1: Add  2: Remove  3: View  > 3
# 
# Input the item to view: > Wizard's sleeve
# You have 2 Wizard's sleeve

import os
import ast

# Auto-load the existing data
def load_data():
    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "r") as f:
            return ast.literal_eval(f.read())
    return []

# Auto-save the data
def save_data(data):
    with open("inventory.txt", "w") as f:
        f.write(str(data))

# Add an item to the inventory
def add_item(inventory):
    item = input("Input the item to add: > ").capitalize()
    inventory.append(item)
    print(f"{item} has been added to your inventory.")
    save_data(inventory)

# Remove an item from the inventory
def remove_item(inventory):
    item = input("Input the item to remove: > ").capitalize()
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has been removed from your inventory.")
    else:
        print(f"{item} is not in your inventory.")
    save_data(inventory)

# View the inventory
def view_inventory(inventory):
    item = input("Input the item to view: > ").capitalize()
    count = inventory.count(item)
    if count > 0:
        print(f"You have {count} {item}(s).")
    else:
        print(f"You have no {item}.")

# Main function
def main():
    print("🌟RPG Inventory🌟")
    inventory = load_data()

    while True:
        print("\n1: Add  2: Remove  3: View  4: Exit")
        choice = input("> ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            remove_item(inventory)
        elif choice == "3":
            view_inventory(inventory)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

main()