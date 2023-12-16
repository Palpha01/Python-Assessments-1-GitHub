# Exercise 4: Registration Page

# Use widgets to create a GUI

import tkinter

from tkinter import *

from PIL import Image

import os

main = Tk()

main.title('Exercise 4')

main.geometry('500x700')

main.resizable(True,True)

Banner = PhotoImage(file="RAK Bathspa.png")

Header = Label(main,image=Banner)
Header.pack(anchor=NW,)

main.resizable(True,True)
main.mainloop()