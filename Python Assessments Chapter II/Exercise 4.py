# Exercise 4: Registration Page

# Use widgets to create a GUI

import tkinter

from tkinter import *

main = Tk()

Banner = PhotoImage(file='Images/RAK Bathspa.jpg')
main.iconphoto(True,Banner)

Banner.pack()

main.resizable(True,True)
main.mainloop()