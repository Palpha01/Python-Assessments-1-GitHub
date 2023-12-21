# Exercise 4: Draw Shape

# Using tkinter module develop GUI to ask the user to select shapes like
# oval, rectangle, square, triangle
# and draw the shape using canvas

import tkinter
from tkinter import *

main = Tk()
main.title("Exercise 4")
main.geometry("500x700")

def draw_triangle(event):
    x1, y1 = event.x, event.y
    triangle = canvas.create_polygon([x1, y1, x1 + 100, y1 + 100, x1 + 50, y1 + 50])
canvas = Canvas(main,width=500,height=500)
canvas.pack()

def draw_oval(event):
    x1, y1 = event.x, event.y
    oval = canvas.create_oval(x1, y1, x1 + 100, y1 + 100)

oval_button = Button(main,text="Draw Oval",command=draw_oval)
oval_button.pack()

def draw_rectangle(event):
    x1, y1 = event.x, event.y
    rectangle = canvas.create_rectangle(x1, y1, x1 + 100, y1 + 100)

rectangle_button = Button(main,text="Draw Rectangle",command=draw_rectangle)
rectangle_button.pack()

square_button = Button(main,text="Draw Square",command=draw_square)
square_button.pack()

triangle_button = Button(main,text="Draw Triangle",command=draw_triangle)
triangle_button.pack()

main.mainloop()