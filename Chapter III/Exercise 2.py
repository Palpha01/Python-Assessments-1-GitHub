# Exercise 2: Coffee Vending Machine

# Develop a coffee Vending Machine that asks users to select the type of coffee, and also prompts users to select various options like sugar, milk, etc. Once selected display the message using a message box. Also, use images in the app.  
# Extension: Add other features to the previous app such as handling money.

import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

main = Tk()

main.title('Exercise 2')
main.geometry('500x500')

Background = ImageTk.PhotoImage(Image.open("Chapter III/Coffee background.png"))

bg = Label(main,image=Background)
bg.place(x=0,y=0)

Greeting = Label(main,text="Welcome to my Coffee Shop!",font=('Helvetica',12,'bold'),bg='#8B4513',fg='chocolate1',width=25,height=5,pady=25)
Greeting.pack()

coffeetype = ["Cappucchino","Latte","Espresso","Mocha","Americano"]
coffvar = StringVar(main)
coffvar.set(coffeetype[0])

dropdown = OptionMenu(main,coffvar,*coffeetype)
dropdown.pack()

milkar = IntVar(value=0)
checkbox = Checkbutton(main,text="Add Milk",variable=milkar)
checkbox.pack()

def order():
    coffee = coffvar.get()
    havemilk = "with milk" if milkar.get() == 1 else ""
    messagebox.showinfo("Enjoy your coffee!", f"You ordered: {coffee} {havemilk}")

orderup = Button(main,text="Order your Coffee",command=order)
orderup.pack()

main.mainloop()