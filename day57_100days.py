#myGPTexperiment
# using Copilot with GPT-4o
# Day 57: Recursion

# Specs:
# Write a factorial function that:
# - Starts at the highest number n.
# - Multiplies that by factorial of itself minus one (n-1).
# - Terminates when it reaches 1 and returns 1.
# - Outputs the factorial.
# - Don't forget to return 1 in your terminating condition.
# - Try multiplying the number by the factorial (n-1) call.

# Example Output:
# 🌟Factorial Finder🌟
# 
# Input a number > 5
# 
# The factorial of 5 is 120.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("🌟Factorial Finder🌟\n")
number = int(input("Input a number > "))
result = factorial(number)
print(f"The factorial of {number} is {result}.")