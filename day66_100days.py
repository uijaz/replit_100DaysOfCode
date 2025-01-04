#myGPTexperiment
# using Copilot with GPT-4o
# Day 66: This is Getting GUI

# Specs:
# - Create a simple GUI calculator using tkinter library.
# - Have buttons for the numbers 0 to 9, plus, minus, multiply, divide and equals.
# - The user should be able to press buttons to create their calculation.
# - It should output the correct result when they press equals.

import tkinter as tk

def button_click(number):
  current = entry.get()
  entry.delete(0, tk.END)
  entry.insert(0, current + str(number))

def button_clear():
  entry.delete(0, tk.END)

def button_equal():
  try:
    result = str(eval(entry.get()))
    entry.delete(0, tk.END)
    entry.insert(0, result)
  except:
    entry.delete(0, tk.END)
    entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=19, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=21, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=21, pady=20, command=lambda: button_click("/"))
button_equal = tk.Button(root, text="=", padx=19, pady=20, command=button_equal)
button_clear = tk.Button(root, text="C", padx=19, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

root.mainloop()