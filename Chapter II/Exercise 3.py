# Exercise 3: Login page

# Create a login page using the Grid geometry

import tkinter

from tkinter import *

main = Tk()

NL = Label(main,text="First name: ").grid(row=0,column=0)
NE = Entry(main).grid(row=0, column=1)

SL = Label(main,text="Surname: ").grid(row=1,column=0)
SE = Entry(main).grid(row=1, column=1)

EL = Label(main,text="Email: ").grid(row=2,column=0)
EE = Entry(main).grid(row=2, column=1)

Submit = Button(main,text="Submit"). grid()

main.mainloop()