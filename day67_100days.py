#myGPTexperiment
# using Copilot with GPT-4o
# Day 67: tkinter

# Specs:
# - This program is to find the image of a floag based on the user's text input.
# - This program uses only the TKinter library and no other library.
# - There are 4 images in the folder 'resources': 'au.png', 'ca.png', 'gb.png', 'us.png'.
# - The program generates a window of size 500 x 500.
# - The window is labelled 'Find the flag'.
# - At the top of the window there is a label in the window that says 'Enter name of a country to find it's flag?'.
# - After the label there is a textbox to prompt the user to input the name.
# - If the user inputs 'Australia', 'Canada', 'UK' or 'USA', then the corresponding image should load. These names are not case sensitive.
# - After the textbox there is a button labelled 'Find'.
# - The textbox above should accept 'enter' to submit the input as the button.
# - After the button there is a label to display if the 'Flag found' or 'Flag not found'.
# - After the label there is a canvas to display the image
# - Resize the images to fit the canvas.
# - If the image is not found show no image, but only the text in the label above 'Flag not found'.

import tkinter as tk
from tkinter import PhotoImage, Label, Entry, Button, Canvas

def find_flag():
  country = entry.get().strip().lower()
  flag_map = {
    'australia': 'resources/flags/au.png',
    'canada': 'resources/flags/ca.png',
    'uk': 'resources/flags/gb.png',
    'usa': 'resources/flags/us.png'
  }
  if country in flag_map:
    img_path = flag_map[country]
    img = PhotoImage(file=img_path)
    img = img.subsample(max(img.width() // 500, 1), max(img.height() // 400, 1))
    canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.image = img
    result_label.config(text="Flag found")
  else:
    canvas.delete("all")
    result_label.config(text="Flag not found")

root = tk.Tk()
root.title("Find the flag")
root.geometry("500x500")

prompt_label = Label(root, text="Enter name of a country to find it's flag.")
prompt_label.pack()

entry = Entry(root)
entry.pack()

entry.bind("<Return>", lambda event: find_flag())

find_button = Button(root, text="Find", command=find_flag)
find_button.pack()

result_label = Label(root, text="")
result_label.pack()

canvas = Canvas(root, width=500, height=400)
canvas.pack()

root.mainloop()