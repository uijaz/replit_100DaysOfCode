#myGPTexperiment
# using Copilot with GPT-4o
# Day 54: CSV Files

# Specs:
# Using the CSV file called 'Day54Totals.csv'.
# - Read the CSV file.
# - Multiply the cost by the quantity.
# - Add it all together to calculate how much money the shop made in a day.
# - Use the dictionary approach to loading your file.
# - Take in 2 different values.
# - Cast them in 2 different ways.

# Example output:
# 🌟Shop ££ Tracker🌟
# Your shop took £592 pounds today.

import csv

# Function to read the CSV file and calculate the total earnings
def calculate_total_earnings(filename):
    total_earnings = 0
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                cost = float(row['Cost'])
                quantity = int(row['Quantity'])
                total_earnings += cost * quantity
    except Exception as e:
        print(f"An error occurred: {e}")
    return total_earnings

# Main function
def main():
    print("🌟Shop ££ Tracker🌟")
    filename = 'Day54Totals.csv'
    total_earnings = round(calculate_total_earnings(filename), 2)
    print(f"Your shop took £{total_earnings} pounds today.")

main()