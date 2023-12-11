# Exercise 2: Managing Layout

# a: Using Pack
# Create a GUI with 4 labels using the pack() geometry

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 2 a')

Button(main, text="A", bg='red', relief=GROOVE, bd=5).pack(side=TOP, expand=YES, fill=X)
Button(main, text="B", bg='yellow').pack(side=BOTTOM, expand=2, anchor=SW)
Button(main, text="C", bg='blue').pack(side=LEFT, expand=2, pady=3, anchor=SE)
Button(main, text="D", bg='white', relief=FLAT).pack(side=RIGHT, expand=2, anchor=S)

main.resizable(True,True)
main.mainloop()