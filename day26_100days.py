# Day 26 - More Libraries
import os
import time
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
pygame.mixer.pause()

def printText(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)
  print()

def menu():
  # clear the screen 
  os.system("clear")
  # Show the menu
  printText("🎵 MyPOD Music Player")
  print()
  time.sleep(0.5)
  printText("Press 1 to Play")
  printText("Press 2 to Pause")
  printText("Press 0 to Exit")
  time.sleep(0.5)
  printText("Press 'Enter' else to refresh the menu.")
  print()


def pause():
  pygame.mixer.pause()
  print("Music paused!")
  time.sleep(0.5)
  return
  
def play():
  # Play the sound
  pygame.mixer.unpause()
  print("Playing music!")
  time.sleep(0.5)
  return

while True:
  menu()
  # take user's input
  user_input = input()
  # check whether you should call the play() subroutine depending on user's input
  if user_input == "1":
    play()
  elif user_input == "2":
    pause()
  elif user_input == "0":
    quit()
  else:
    os.system("clear")
    time.sleep(1)
    continue