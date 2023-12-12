# Exercise 2: Managing Layout

# a: Using Pack
# Create a GUI with 4 labels using the pack() geometry

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 2 a')

Button(main, text="A", bg='red', relief=GROOVE, bd=5).pack(side=TOP, expand=YES, fill=X)
Button(main, text="B", bg='yellow', padx=50).pack(side=BOTTOM, expand=2, anchor=S)
Button(main, text="C", bg='blue',  padx=50, relief=FLAT).pack(side=LEFT, expand=2, anchor=SE)
Button(main, text="D", bg='white', relief=FLAT, padx=50).pack(side=RIGHT, expand=2, anchor=S)

main.resizable(True,True)
main.mainloop()