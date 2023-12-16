# Exercise 2: Managing Layout

# B: Square Grid
# With the pack layout manager, Create the following labels inside the frames. A and B inside the left frame. C and D inside the right frame

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 2 b')

Frame1 = Frame(main,border=5,relief="solid").pack(side=LEFT,expand=FALSE,fill="both")

A = Label(Frame1,text="A",bg="#22263d",fg="white").pack(side=TOP,expand=TRUE,fill="both")
B = Label(Frame1,text="B",bg="white",fg="#22263d").pack(side=BOTTOM,expand=TRUE,fill="both")

Frame2 = Frame(main,border=5,relief="solid").pack(side=RIGHT,expand=FALSE,fill="both")

C = Label(Frame2,text="C",bg="white",fg="#22263d").pack(side=TOP,expand=TRUE,fill="both")
D = Label(Frame2,text="D",bg="#22263d",fg="white").pack(side=BOTTOM,expand=TRUE,fill="both")

main.resizable(True,True)
main.mainloop()