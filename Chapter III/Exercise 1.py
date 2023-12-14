# Exercise 1: Greeting App

# Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.

import tkinter

from tkinter import *

from tkinter import ttk

main = Tk()

def update_greeting():
    name = name_entry.get()
    color = colovar.get()
    greeting_label.config(text="Hello " + name + "!",fg=color)

main.title('Exercise 1')
main.geometry('500x500')

Finput = Frame(main,bg='skyblue')
Finput.pack(pady=10)

Fisplay = Frame(main,bg='goldenrod')
Fisplay.pack(pady=10)

Tabel = Label(Finput,text="Greeting App",fg='blue',font=("Helvetica",20),bg="skyblue")
Tabel.grid(row=0,column=0,columnspan=2,pady=10)

Nabel = Label(Finput,text="State your name",bg='skyblue')
Nabel.grid(row=1,column=0,pady=5)

name_entry = Entry(Finput)
name_entry.grid(row=1,column=1,pady=5)

Cabel = Label(Finput,text="Choose your color: ",bg='skyblue')
Cabel.grid(row=2,column=0,pady=5)

colors = ['blue','fuchsia','maroon','gold','olive']
colovar = StringVar()
coloropdown = ttk.Combobox(Finput,textvariable=colovar, values=colors,state="readonly")
coloropdown.current(0)
coloropdown.grid(row=2,column=1,pady=5)

update = Button(Finput,text="Update Greeting", command=update_greeting)
update.grid(row=3,column=0,columnspan=2,pady=10)

greeting_label = Label(Fisplay,text="",font=("Helvetica",15),bg='goldenrod')
greeting_label.pack(pady=20)

main.mainloop()