# Exercise 4: Draw Shape

# Using tkinter module develop GUI to ask the user to select shapes like
# oval, rectangle, square, triangle
# and draw the shape using canvas

import tkinter
from tkinter import *
from tkinter import ttk, messagebox

def draw_shape():
    try:
        selected = shapeselection.get()
        coordinates = coordinatentry.get()
        coordinatelist = [int(coord.strip()) for coord in coordinates.split(',')]

        if selected == "Star":
            canvas.create_polygon(coordinatelist,outline='gold')
        elif selected == "Square":
            canvas.create_rectangle(coordinatelist,outline='blue')
        elif selected == "Circle":
            canvas.create_oval(coordinatelist,outline='red')
        elif selected == "Triangle":
            canvas.create_polygon(coordinatelist,outline='green')
        else:
            messagebox.showerror("Nope","Please choose a valid shape")
            return
    except ValueError:
        messagebox.showerror("Where are you going?","Please enter valid coordinates")

main = Tk()
main.title("Exercise 4")
main.geometry("1000x1000")

canvas = Canvas(main,width=500,height=500,bg='white')
canvas.pack()

shapabel = Label(main,text="Select Shape:")
shapabel.pack()
shapeselection = ttk.Combobox(main, values=["Star","Square","Circle","Triangle"])
shapeselection.pack()

coordinatabel = Label(main,text="Enter Coordinates (comma-separated):")
coordinatabel.pack()
coordinatentry = Entry(main)
coordinatentry.pack()

draw = Button(main,text="Draw",command=draw_shape)
draw.pack(pady=10)

main.mainloop()