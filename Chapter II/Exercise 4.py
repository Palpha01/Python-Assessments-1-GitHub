# Exercise 4: Registration Page

# Use widgets to create a GUI

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 3')

main.geometry('500x700')

main.resizable(True,True)

img = PhotoImage(file='RAK Bathspa.png')
Label (image=img).pack()

h1 = Label(main, text="Student Management System").pack()
h2 = Label(main, text="New Student Registration").pack()

name = Label(main, text="Student Name").pack()
namentry = Entry(main).pack()

mobile = Label(main, text="Mobile Number").pack()
mobilentry = Entry(main).pack()

email = Label(main, text="Email ID").pack()
emailentry = Entry(main).pack()

home = Label(main, text="Home Address").pack()
homentry = Entry(main).pack()

gender = Label(main, text="Gender").pack()
genderentry = Entry(main).pack()

course = Label(main, text="Course Enrolled").pack()
CC = Radiobutton(main, text="BSc CC", variable="v", value=1).pack()
CY = Radiobutton(main, text="BSc CY", variable="v", value=2).pack()
PSY = Radiobutton(main, text="BSc PSY", variable="v", value=3).pack()
AM = Radiobutton(main, text="BA & BM", variable="v", value=4).pack()

language = Label(main, text="Languages known").pack()
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
ENG = Checkbutton(main, text="English", variable="Var1", onvalue=1, offvalue=0, height=1, width=20).pack()
FIL = Checkbutton(main, text="Tagalog", variable="Var2", onvalue=1, offvalue=0, height=1, width=20).pack()
IND = Checkbutton(main, text="Hindi/Urdu", variable="Var3", onvalue=1, offvalue=0, height=1, width=20).pack()

submit = Button(main, text="Submit", height=1, width=5).pack()
clear = Button(main, text="Clear", height=1, width=5).pack()

main.resizable(True,True)
main.mainloop()