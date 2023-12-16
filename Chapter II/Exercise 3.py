# Exercise 3: Login page

# Create a login page using the Grid geometry

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 3')

NL = Label(main,text="First name: ")
NE = Entry(main)
NL.grid(row=0,column=0)
NE.grid(row=0,column=1)

SL = Label(main,text="Surname: ")
SE = Entry(main)
SL.grid(row=1, column=0)
SE.grid(row=1, column=1)

EL = Label(main,text="Email: ")
EE = Entry(main)
EL.grid(row=2,column=0)
EE.grid(row=2, column=1)

Submit = Button(main,text="Submit")
Submit.grid(columnspan=5)

main.mainloop()