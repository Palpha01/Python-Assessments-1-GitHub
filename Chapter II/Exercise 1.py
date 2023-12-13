# Exercise 1: Welcome

# Develop a GUI program to do the following using the tkinter module

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 1')
main.geometry('500x200')

message=Label(main,text="Welcome to Tkinter", bg='skyblue', width=20, height=30, font=('Times',20,'bold'))
message.pack()

main.configure(bg='dodgerblue')
main.resizable(False,False)
main.mainloop()