# Exercise 4: Registration Page

# Use widgets to create a GUI

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

main = Tk()
main.title("Exercise 4")

Banner = ImageTk.PhotoImage(Image.open("Python-Assessments-1-GitHub/Chapter II/RAK_Bathspa.jpg"))

Heading = Label(main,image=Banner,bg="#22263d")
Heading.pack(side=TOP,fill=BOTH,expand=NO)

Framehead = Frame(main)
Framehead.pack()



Framebody = Frame(main)
Framebody.pack()



Framelanguage = Frame(main)
Framelanguage.pack()



Framescroll = Frame(main)
Framescroll.pack()



Framebuttons = Frame(main)
Framebuttons.pack()



main.geometry("400x600")

main.mainloop()