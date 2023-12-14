# Exercise 1: User information

# Develop a GUI App to create a file called 'bio.txt' and write the following information to the file asking user to enter the values
# Each piece of data should be on a new line. Once the data has been written to the file, read the data from the file and output the data

# Values: Name Age Hometown

import tkinter

from tkinter import *

import tkinter.messagebox

bio = Tk()

bio.title('Exercise 1')

bio.geometry('500x500')

bio.resizable(True,True)

name = Label(bio,text="Name:").grid(row=0,column=0,padx=5)
name_entry = Entry(bio,width=30).grid(row=0,column=1)

age = Label(bio,text="Age:").grid(row=1,column=0,padx=5)
age_entry = Entry(bio,width=30).grid(row=1,column=1)

hometown = Label(bio,text="Hometown:").grid(row=2,column=0,padx=5)
hometown_entry = Entry(bio,width=30).grid(row=2,column=1)

def onClick():
    tkinter.messagebox.showinfo("")

button = Button(bio, text="Read", command=onClick, height=1, width=5)
button.grid(row=3,column=1)

bio.mainloop()