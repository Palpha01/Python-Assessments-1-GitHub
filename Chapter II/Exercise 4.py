# Exercise 4: Registration Page

# Use widgets to create a GUI

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

main = Tk()
main.title("Exercise 4")

Banner = ImageTk.PhotoImage(Image.open("Chapter II/RAK_Bathspa.jpg"))

Heading = Label(main,image=Banner,bg="#22263d")
Heading.pack(side=TOP,fill=BOTH,expand=NO)

Framehead = Frame(main,bg="#f5f5f6")
Framehead.pack()

Header = Label(Framehead,text="Student Management System",font=("Arial",14,"bold"),fg="#22263d",bg="#f5f5f6",pady=5)
Header2 = Label(Framehead,text="New Student Registration",font=("Arial",12,"bold"),fg="#22263d",bg="#f5f5f6",pady=5)
Header.pack()
Header2.pack()

Framebody = Frame(main,bg="#f5f5f6")
Framebody.pack()

Name = Label(Framebody,text="Student Name:",font=("Arial",10),fg="#22263d",bg="#f5f5f6")
Namentry = Entry(Framebody,bg="grey",relief=FLAT)
Mobile = Label(Framebody,text="Mobile Number:",font=("Arial",10),fg="#22263d",bg="#f5f5f6")
Mobilentry = Entry(Framebody,bg="grey",relief=FLAT)
Email = Label(Framebody,text="Email ID:",font=("Arial",10),fg="#22263d",bg="#f5f5f6")
Emailentry = Entry(Framebody,bg="grey",relief=FLAT)
Address = Label(Framebody,text="Home Address:",font=("Arial",10),fg="#22263d",bg="#f5f5f6")
Addressentry = Entry(Framebody,bg="grey",relief=FLAT)
Gender = Label(Framebody,text="Gender:",font=("Arial",10),fg="#22263d",bg="#f5f5f6")
Genderentry = Entry(Framebody,bg="grey",relief=FLAT)

Name.grid(row=0,column=0,padx=20,pady=5)
Namentry.grid(row=0,column=1,pady=5)
Mobile.grid(row=1,column=0,padx=20,pady=5)
Mobilentry.grid(row=1,column=1,pady=5)
Email.grid(row=2,column=0,padx=20,pady=5)
Emailentry.grid(row=2,column=1,pady=5)
Address.grid(row=3,column=0,padx=20,pady=5)
Addressentry.grid(row=3,column=1,pady=5)
Gender.grid(row=4,column=0,padx=20,pady=5)
Genderentry.grid(row=4,column=1,padx=20,pady=5)


Framecourses = Frame(main,bg="#f5f5f6")
Framecourses.pack()

Courses = Label(Framecourses,text="Course Enrolled:",font=("Arial",10),fg="#22263d",bg="#f5f5f6")

Courses.grid(row=0,column=0)

V = StringVar(Framecourses, "1")

Variablecourses = {"BSc CC" : "1", 
        "BSc CY" : "2", 
        "BSc PSY" : "3", 
        "BA & BM" : "4"} 

for (text,value) in Variablecourses.items():
    Radiobutton(Framecourses,text="BSc CC",variable=V,value=1,font=("Arial",10),fg="#22263d",bg="#f5f5f6").grid(row=0,column=1)
    Radiobutton(Framecourses,text="BSc CY",variable=V,value=2,font=("Arial",10),fg="#22263d",bg="#f5f5f6").grid(row=1,column=1)
    Radiobutton(Framecourses,text="BSc PSY",variable=V,value=3,font=("Arial",10),fg="#22263d",bg="#f5f5f6").grid(row=2,column=1)
    Radiobutton(Framecourses,text="BA & BM",variable=V,value=4,font=("Arial",10),fg="#22263d",bg="#f5f5f6").grid(row=3,column=1)

Framelanguage = Frame(main,bg="#f5f5f6")
Framelanguage.pack()

Languages = Label(Framelanguage,text="Languages Known:",font=("Arial",10),fg="#22263d",bg="#f5f5f6")  
Languages.grid(row=0,column=0)

Button1 = IntVar()   
Button2 = IntVar()   
Button3 = IntVar()

English = Checkbutton(Framelanguage,text="English",variable=Button1,font=("Arial",10),fg="#22263d",bg="#f5f5f6") 
English.grid(row=0,column=1)
Tagalog = Checkbutton(Framelanguage,text="Tagalog",variable=Button2,font=("Arial",10),fg="#22263d",bg="#f5f5f6")
Tagalog.grid(row=0,column=2)
Indian = Checkbutton(Framelanguage,text="Hindi/Urdu",variable=Button3,font=("Arial",10),fg="#22263d",bg="#f5f5f6")
Indian.grid(row=1,column=1)

Framescalet = Frame(main,bg="#f5f5f6")
Framescalet.pack()

Hmm = Label(Framescalet,text="Rate your English communication skills",font=("Arial",12,"bold"),fg="#22263d",bg="#f5f5f6")
Hmm.pack()

Scalet = Scale(Framescalet,from_=1,to=100,orient=HORIZONTAL)
Scalet.pack(pady=10)

Framebuttons = Frame(Framescalet,bg="#f5f5f6")
Framebuttons.pack()

Submit = Button(Framebuttons,text="Submit",font=("Arial",12,"bold"),fg="white",bg="#22263d",relief=FLAT)
Clear = Button(Framebuttons,text="Clear",font=("Arial",12,"bold"),fg="white",bg="#22263d",relief=FLAT)
Submit.grid(row=0,column=0,padx=20,ipadx=20)
Clear.grid(row=0,column=1,ipadx=20)

main.geometry("500x900")

main.mainloop()