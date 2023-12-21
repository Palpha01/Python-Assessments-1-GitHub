# Exercise 3: Area Function

# Develop a GUI application using tkinter that allows users to calculate and display the areas of various shapes
# including circles, squares, and rectangles

import tkinter
from tkinter import *
from tkinter import ttk,messagebox

def calculate_area():
    try:
        if selected.get() == "Circle":
            radius = float(radiusentry.get())
            area = 3.14 * radius**2
        elif selected.get() == "Square":
            side = float(sidentry.get())
            area = side**2
        elif selected.get() == "Rectangle":
            length = float(lengthentry.get())
            width = float(widthentry.get())
            area = length * width
        else:
            messagebox.showerror("That's not a shape...")
            return
        
        resultabel.config(text=f"Area: {area:.2f} square units")
    except ValueError:
        messagebox.showerror("Is that a dimension?")

main = Tk()
main.title("Exercise 3")
main.geometry("300x350")

tab = ttk.Notebook(main)

circle = Frame(tab)
square = Frame(tab)
rectangle = Frame(tab)

tab.add(circle,text="Circle")
tab.add(square,text="Square")
tab.add(rectangle,text="Rectangle")

tab.pack(expand=3,fill=BOTH)

selected = StringVar(value="Square")
shabel = Label(main,text="Choose a Shape: ")
shabel.pack()
shapelection = ttk.Combobox(main,textvariable=selected,values=["Circle","Square","Rectangle"])
shapelection.pack()

# This is a circle

radiusabel = Label(circle,text="Enter Radius: ")
radiusabel.pack(pady=10)
radiusentry = Entry(circle)
radiusentry.pack(pady=10)

# This is a square

sideabel = Label(square,text="Enter the Length of the Side: ")
sideabel.pack(pady=10)
sidentry = Entry(square)
sidentry.pack(pady=10)

# This is a rectangle

lengthabel = Label(rectangle,text="Enter the Length: ")
lengthabel.pack(pady=10)
lengthentry = Entry(rectangle)
lengthentry.pack(pady=10)

widthabel = Label(rectangle,text="Enter the Width: ")
widthabel.pack(pady=10)
widthentry = Entry(rectangle)
widthentry.pack(pady=10)

calculate = Button(main,text="Calculate",command=calculate_area)
calculate.pack(pady=10)

resultabel = Label(main,text="The Area is: ")
resultabel.pack(pady=10)

main.mainloop()