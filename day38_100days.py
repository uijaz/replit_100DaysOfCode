# Day 38 - Strings and Loops
def changeColour(letter):
    colours = {
        "r": "\033[31m",
        "g": "\033[32m",
        "y": "\033[33m",
        "b": "\033[34m",
        "p": "\033[35m",
        " ": "\033[0m"
    }
    colour_code = colours.get(letter.lower(), "")
    return f"{colour_code}{letter}"

while True:
    sentence = input("What is your favourite sentence: ")
    for letter in sentence:
        if letter.lower() in ["r", "g", "b", "p", "y", " "]:
            letter = changeColour(letter)
        print(letter, end="")
    print(changeColour(" "))