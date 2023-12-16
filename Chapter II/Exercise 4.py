# Exercise 4: Registration Page

# Use widgets to create a GUI

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

main = Tk()
main.title("Exercise 4")

Banner = ImageTk.PhotoImage(Image.open("Python-Assessments-1-GitHub/Chapter II/RAK_Bathspa.jpg"))

Heading = Label(main,image=Banner)
Heading.pack(side=TOP,fill=BOTH,expand=NO)

main.geometry("400x600")

main.mainloop()