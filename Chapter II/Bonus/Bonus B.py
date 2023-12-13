# Exercise B: Age Calculator

# Create a program to take input of the user's date of birth and output the age

import tkinter

from tkinter import *

from datetime import date
today = date.today()

def exit():
    main.destroy()
    
def get_age():
    d= int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    age =today.year-y-((today.month, today.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', END)
    t1.insert(END,age)
    t1.config(state='disabled')
    
main = Tk()
main.geometry("400x300")
main.config(bg="navyblue")
main.resizable(True,True)
main.title('Bonus B')

l1 = Label(main,text="The Age Calculator",font=('Helvetica',20,'bold'),fg="skyblue",bg="navyblue")
l2 = Label(main,font=('Helvetica',12,'bold'),text="Please designate your birthday",fg="skyblue",bg="navyblue")

day = Label(main,text="Date: ",font=('Helvetica',12),fg="skyblue",bg="navyblue")
month = Label(main,text="Month: ",font=('Helvetica',12),fg="skyblue",bg="navyblue")
year = Label(main,text="Year: ",font=('Helvetica',12),fg="skyblue",bg="navyblue")
e1 = Entry(main,width=5)
e2 = Entry(main,width=5)
e3 = Entry(main,width=5)

b1 = Button(main,text="Calculate",font=('Helvetica',13),command=get_age)

l3 = Label(main,text="Your current age is: ",font=('Helvetica',12,'bold'),fg="skyblue",bg="navyblue")
t1 = Text(main,width=5,height=0,state="disabled")

l1.place(x=70,y=5)
l2.place(x=80,y=40)
day.place(x=100,y=70)
month.place(x=100,y=95)
year.place(x=100,y=120)
e1.place(x=180,y=70)
e2.place(x=180,y=95)
e3.place(x=180,y=120)
b1.place(x=100,y=150)
l3.place(x=50,y=200)
t1.place(x=240,y=205)

main.mainloop()