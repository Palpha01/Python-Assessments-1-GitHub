# Exercise 2: Managing Layout

# a: Using Pack
# Create a GUI with 4 labels using the pack() geometry

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 2 a')

Label(main, text="A", width=12, bg='red', relief=GROOVE, bd=5).pack(side=TOP, expand=1, fill=X)
Label(main, text="B", width=12, bg='yellow').pack(side=BOTTOM)
Label(main, text="C", width=12, bg='blue').pack(side=LEFT, expand=1, fill=Y)
Label(main, text="D", width=12, bg='white').pack(side=RIGHT)

main.resizable(True,True)
main.mainloop()