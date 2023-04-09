import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk
import os
import random

SIZE = 4
BUTTON_SIZE=50
PIC_COUNT = int(SIZE*SIZE/2)

window = tk.Tk()
window.title("Memory")

buttons = [[0 for x in range(SIZE)] for y in range(SIZE)]
photo_images = [[0 for x in range(SIZE)] for y in range(SIZE)]

pictures = []
pic_path = os.listdir("./pictures/")
for i in range(2):
    for i in range(PIC_COUNT):
        pictures.append(pic_path[i])

pic_count = PIC_COUNT*2

for x in range(SIZE):
    window.rowconfigure(weight=1, index=x)
    for y in range(SIZE):
        print(str(x)+" | "+str(y))
        i = random.randint(0, pic_count-1)
        path = os.path.join("./pictures", pictures[i])
        photo_images[x][y] = ImageTk.PhotoImage(file=path)
        buttons[x][y] = ttk.Button(window, image=photo_images[x][y])
        pictures.pop(i)
        pic_count -= 1
        buttons[x][y].grid(row=x, column=y, sticky = "NSEW")
        window.columnconfigure(weight=1, index=y)

buttons[0][0]



window.mainloop()