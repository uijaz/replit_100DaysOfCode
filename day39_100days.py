# Day 39 - Project Day: Hangman!
import random

def randomWordSelector():
  listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
  return(random.choice(listOfWords))

def createResult(letter, word, old_result):
  new_result = ""
  for e in word:
    if letter == e:
      new_result += letter
    elif e in old_result:
      new_result += e
    else:
      new_result += "-"
  return new_result

def finalVerdict(count):
  if count > 0:
    print(f"You won with {count} lives left.")
  else:
    print(f"You lost!")  

def guessMsg(state, count, word):
  if state:
    print(f"Correct!")
    print(f"{word}")
    print()
  else:
    print(f"Nope, not in there.")
    if len(word) > 0:
      print(f"{word}")
  print(f"You have {count} goes left.")
  print()

def gameEngine(gameWord):
  count = 6
  word_in_progress = ""
  while True:

    if count > 0 and word_in_progress != gameWord:
      userLetter = input("Choose a letter: ")
      print()
      
      if userLetter != "":

        # already guessed
        if userLetter in word_in_progress:
          print(f"You have already guessed '{userLetter}'")
          print(f"Try again!")
          print()
        # guessed correctly
        elif userLetter in gameWord:
          word_in_progress = createResult(userLetter, gameWord, word_in_progress)
          guessMsg(True, count, word_in_progress)
        # guessed wrong
        else:
          count -= 1
          guessMsg(False, count, word_in_progress)

      else:
        print(f"Try again!")
        print()

    elif word_in_progress == gameWord:
      finalVerdict(count)
      return
    elif count == 0:
      finalVerdict(count)
      return

def hangman():
  print("🌟Hangman🌟")
  print()
  gameWord = randomWordSelector()
#  print(f">>{gameWord}<<") # for testing
  print()
  gameEngine(gameWord)

hangman()