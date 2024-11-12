# Day 4 - 'Print' in Color! 
print("Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")
print()
print("\033[31m")
name = input("What is your name? ")
worstEnemyName = input("What is your worst enemy’s name? ")
superpower = input("What is your superpower? ")  
whereYouLive = input("Where do you live? ")
yourFavoriteFood = ("What is your favorite food? ")
print("\033[0m")
# Using f-string
message = f"Hello {name}! Your ability to {superpower} will make sure you never have to look at {worstEnemyName} again. Go eat {yourFavoriteFood} as you walk down the streets of {whereYouLive} and use {superpower} for good and not evil!"
print(message)
