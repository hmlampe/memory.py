import tkinter as tk
from tkinter import ttk
from tkinter import Grid

SIZE = 3

window = tk.Tk()
window.title("Memory")


buttons = [[0 for x in range(SIZE)] for y in range(SIZE)]

for x in range(SIZE):
    window.rowconfigure(weight=1, index=x)
    for y in range(SIZE):
        print(str(x)+" | "+str(y))
        buttons[x][y] = ttk.Button(window, text="Button")
        buttons[x][y].grid(row=x, column=y, sticky = "NSEW")
        window.columnconfigure(weight=1, index=y)


window.mainloop()