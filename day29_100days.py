# Day 29 - The Secrets of `print`
def printColour(text, colour):
  if colour == "red":
    print("\033[31m", text, "\033[0m", sep="", end="") # red
  elif colour == "green":
    print("\033[32m", text, "\033[0m", sep="", end="") # green
  elif colour == "yellow":
    print("\033[33m", text, "\033[0m", sep="", end="") #yellow
  elif colour == "blue":
    print("\033[34m", text, "\033[0m", sep="", end="") # blue

print("Hello there", end=" ")
printColour("RED", "red")
print(",", end=" ")
printColour("GREEN", "green")
print(",", end=" ")
printColour("YELLOW", "yellow")
print(" and", end=" ")
printColour("BLUE", "blue")
print("!", end="")