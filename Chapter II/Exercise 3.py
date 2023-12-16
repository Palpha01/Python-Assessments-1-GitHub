# Exercise 3: Login page

# Create a login page using the Grid geometry

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 3')
main.geometry("220x150")

NL = Label(main,text="First name: ")
NE = Entry(main)
NL.grid(row=0,column=0,padx=5,pady=5)
NE.grid(row=0,column=1,padx=5,pady=5)

SL = Label(main,text="Surname: ")
SE = Entry(main)
SL.grid(row=1, column=0,padx=5,pady=5)
SE.grid(row=1, column=1,padx=5,pady=5)

EL = Label(main,text="Email: ")
EE = Entry(main)
EL.grid(row=2,column=0,padx=5,pady=5)
EE.grid(row=2, column=1,padx=5,pady=5)

Submit = Button(main,text="Submit",padx=5,pady=5,bg="#22263d",fg="white")
Submit.grid(columnspan=5,pady=10)

main.mainloop()