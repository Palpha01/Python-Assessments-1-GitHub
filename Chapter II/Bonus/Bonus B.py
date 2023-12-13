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
main.config(bg="#F7DC6F")
main.resizable(True,True)
main.title('Bonus B')

l1 = Label(main,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
l2 = Label(main,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")

day = Label(main,text="Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
month = Label(main,text="Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
year = Label(main,text="Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
e1 = Entry(main,width=5)
e2 = Entry(main,width=5)
e3 = Entry(main,width=5)

b1 = Button(main,text="Calculate Age!",font=("Arial",13),command=get_age)

l3 = Label(main,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
t1 = Text(main,width=5,height=0,state="disabled")

b2 = Button(main,text="Exit Application!",font=("Arial",13),command=exit)

l1.place(x=70,y=5)
l2.place(x=10,y=40)
day.place(x=100,y=70)
month.place(x=100,y=95)
year.place(x=100,y=120)
e1.place(x=180,y=70)
e2.place(x=180,y=95)
e3.place(x=180,y=120)
b1.place(x=100,y=150)
l3.place(x=50,y=200)
t1.place(x=240,y=203)
b2.place(x=100,y=230)

main.mainloop()