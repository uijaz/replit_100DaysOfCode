#myGPTexperiment
# using Copilot with GPT-4o
# Day 69: Project Day: Graphic Novel

# Specs:
# Create a visual novel using TKinter library and no other library.
# - Use 1000 x 1000 winow size.
# - This is a 'choose your own adventure' style game that will show images of flags and a bit of text, allowing the user to make decisions that influence what will be displayed next.
# Requirements:
# 1. Start with a random flag from one of the four flags in the 'resources/flags' folder, accompanied by a short text introduction and two options for the user to choose from.
# List of flaf images:  'au.png', 'ca.png', 'gb.png', 'us.png'.
# 2. Allow the user to click buttons to choose their options.
# 3. Based on the user's choice, display the appropriate branch with the corresponding flag image, text, and further option buttons.
# 4. One branch should have both second options leading to the same flag image with a story within that country, ensuring the user never gets to travel abroad.
# 5. The ending for this branch should display the same flag image, some concluding text, and a 'start again' button that takes the user back to the beginning.
# 6. The second branch should have two options: one that leads to travelling abroad, and one where travelling was cancelled.
# 7. Both options in the second branch should also have a 'start again' button.
# 8. Ensure the user interface is intuitive and visually appealing.
# 9. Handle any potential errors gracefully, providing feedback to the user if necessary.

import tkinter as tk
from tkinter import messagebox
import random
import os

class VisualNovel:
  def __init__(self, root):
    self.root = root
    self.root.title("Choose Your Own Adventure")
    self.root.geometry("1000x1000")
    self.flags = ['au.png', 'ca.png', 'gb.png', 'us.png']
    self.flag_path = 'resources/flags/'
    self.setup_ui()

  def setup_ui(self):
    self.canvas = tk.Canvas(self.root, width=1000, height=1000)
    self.canvas.pack()
    self.start_game()

  def start_game(self):
    self.current_flag = random.choice(self.flags)
    self.display_scene(self.current_flag, "Welcome to the adventure!", ["Option 1", "Option 2"], [self.branch_one, self.branch_two])

  def display_scene(self, flag, text, options, commands):
    self.canvas.delete("all")
    flag_image = tk.PhotoImage(file=os.path.join(self.flag_path, flag))
    self.canvas.create_image(500, 300, image=flag_image)
    self.canvas.image = flag_image
    self.canvas.create_text(500, 600, text=text, font=("Arial", 20), fill="black")
    for i, option in enumerate(options):
      button = tk.Button(self.root, text=option, command=commands[i])
      self.canvas.create_window(500, 650 + i*50, window=button)

  def branch_one(self):
    self.display_scene(self.current_flag, "You chose option 1. What next?", ["Option 1A", "Option 1B"], [self.same_country, self.same_country])

  def branch_two(self):
    self.display_scene(self.current_flag, "You chose option 2. What next?", ["Travel Abroad", "Cancel Travel"], [self.travel_abroad, self.cancel_travel])

  def same_country(self):
    self.display_scene(self.current_flag, "You stayed in the same country. The end.", ["Start Again"], [self.start_game])

  def travel_abroad(self):
    new_flag = random.choice([flag for flag in self.flags if flag != self.current_flag])
    self.display_scene(new_flag, "You traveled abroad. The end.", ["Start Again"], [self.start_game])

  def cancel_travel(self):
    self.display_scene(self.current_flag, "Travel was cancelled. The end.", ["Start Again"], [self.start_game])

if __name__ == "__main__":
  root = tk.Tk()
  app = VisualNovel(root)
  root.mainloop()