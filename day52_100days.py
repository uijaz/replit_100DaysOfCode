#myGPTexperiment
# using Copilot with GPT-4o
# Day 52: Avoiding Crashes

# Specs:
# - Prompt the user to input the quantity and size of pizzas.
# - Multiply the two inputs together to calculate the cost of the pizzas.
# - Store that in a 2D list with the user's name.
# - Use try.... except for two reasons:
# -- Include auto-save and auto-load. Use it with the auto-load.
# -- When casting the quantity of pizzas to an integer. Avoid the user crashing the program by typing 'three' instead of '3'. Or any other non-integer input. If they do, then prompt them to try again.
# - Use subroutines for 'add' and 'view'
# - Use a while.... true loop for the main menu
# - Use a 2d list to store the details of each pizza.
# - Use selection to decide which subroutine to run, then write the 2d list to the file.
# - For add, get all the inputs in variables and append to a list. Append this list to a 2d one that stores all the pizza details.
# - For view, get each index from one row of the 2d list at a time.

# Example output:
# 🌟Dave's Dodgy Pizzas🌟
# How many pizzas? > three
# You must input a numerical character, try again. > 3
# What size? > XXXXXX
# Name please > David
# Thanks David, your pizzas will cost XXXXX

import os
import ast

# Auto-load the existing data
def load_data():
    if os.path.exists("pizzas.txt"):
        with open("pizzas.txt", "r") as f:
            return ast.literal_eval(f.read())
    return []

# Auto-save the data
def save_data(data):
    with open("pizzas.txt", "w") as f:
        f.write(str(data))

# Add a new pizza order
def add_pizza(pizzas):
    while True:
        try:
            quantity = int(input("How many pizzas? > "))
            break
        except ValueError:
            print("You must input a numerical character, try again.")

    while True:
        size = input("What size? (8, 12, 16) > ")
        if size in ["8", "12", "16"]:
            size = int(size)
            break
        else:
            print("Invalid size, please enter 8, 12, or 16.")

    name = input("Name please > ")

    cost = quantity * size
    pizzas.append([name, quantity, size, cost])

    print(f"Thanks {name}, your pizzas will cost £{cost}.")
    save_data(pizzas)

# View all pizza orders
def view_pizzas(pizzas):
    if not pizzas:
        print("No pizza orders found.")
    else:
        for order in pizzas:
            print(f"Name: {order[0]}, Quantity: {order[1]}, Size: {order[2]}, Cost: {order[3]}")

# Main function
def main():
    print("🌟Dave's Dodgy Pizzas🌟")
    pizzas = load_data()

    while True:
        print("\nMenu:")
        print("1. Add a pizza order")
        print("2. View all pizza orders")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_pizza(pizzas)
        elif choice == "2":
            view_pizzas(pizzas)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

main()