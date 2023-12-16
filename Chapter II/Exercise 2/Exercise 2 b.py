# Exercise 2: Managing Layout

# B: Square Grid
# With the pack layout manager, Create the following labels inside the frames. A and B inside the left frame. C and D inside the right frame

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 2 b')

Frame1 = Frame(main,borderwidth=5,relief="solid").pack(side=LEFT,expand=True,fill='both')
Frame2 = Frame(main,borderwidth=5,relief="solid").pack(side=RIGHT,expand=True,fill='both')

A = Label(Frame1,text="A",bg="#22263d",fg="white").pack(side=TOP,expand=True,fill="both")
B = Label(Frame1,text="B",bg="white",fg="#22263d").pack(side=BOTTOM,expand=True,fill="both")
C = Label(Frame2,text="C",bg="#22263d",fg="white").pack(side=TOP,expand=True,fill="both")
D = Label(Frame2,text="D",bg="white",fg="#22263d").pack(side=BOTTOM,expand=True,fill="both")

main.resizable(True,True)
main.mainloop()