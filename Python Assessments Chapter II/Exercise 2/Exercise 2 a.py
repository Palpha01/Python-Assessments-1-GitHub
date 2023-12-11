# Exercise 2: Managing Layout

# a: Using Pack
# Create a GUI with 4 labels using the pack() geometry

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 2 a')

Button(main, text="A", bg='red').pack(side=LEFT, expand=YES, fill=Y)
Button(main, text="B", bg='yellow').pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text="C", bg='blue').pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE, pady=6)
Button(main, text="D", bg='white').pack(side=BOTTOM, expand=NO, fill=Y, pady=6)

main.resizable(True,True)
main.mainloop()