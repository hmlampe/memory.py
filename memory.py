import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk
import os
import random

SIZE = 4
BUTTON_SIZE=50
PIC_COUNT = int(SIZE*SIZE/2)

class MemButton(ttk.Button):

    open = False

    def __init__(self, *args, **kwargs):
        ttk.Button.__init__(self, *args, **kwargs)
        self['text'] = "Karte"
        self['command'] = self.change

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_picture(self, picture):
        self.picture = picture

    def change(self):
        if self.open:
            self['image'] = None
            self['text'] = ""
        else:
            self['image'] = self.picture
            self['text'] = "Karte"
        self.open = not self.open
        self.update()
    
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
        buttons[x][y] = MemButton(window)
        buttons[x][y].set_position(x, y)
        buttons[x][y].set_picture(photo_images[x][y])
        pictures.pop(i)
        pic_count -= 1
        height = 300-buttons[x][y].winfo_reqheight()
        width = 300-buttons[x][y].winfo_reqwidth()
        buttons[x][y].grid(row=x, column=y, ipadx=width, ipady=height, sticky = "NSEW")
        window.columnconfigure(weight=1, index=y)

buttons[0][0]



window.mainloop()