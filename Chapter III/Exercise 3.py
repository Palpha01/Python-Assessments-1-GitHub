# Exercise 3: Area Function

# Develop a GUI application using tkinter that allows users to calculate and display the areas of various shapes
# including circles, squares, and rectangles

# import tkinter

# from tkinter import *

# from math import pi

# def calculate_area():
#     shape = shape_var.get()
#     if shape == "circle":
#         radius = float(Rentry.get())
#         area = pi * radius ** 2
#     elif shape == "square":
#         side = float(Sentry.get())
#         area = side ** 2
#     elif shape == "rect":
#         length = float(Lentry.get())
#         width = float(Wentry.get())
#         area = length * width
#     else:
#         area = 0
    
#     result.config(text="The area of " + shape + " is " + area + " square units")
    
# main = Tk()
# main.title("Exercise 3")

# frame = Label(main)
# frame.pack(pady=10)

# shape_label = Label(frame, text="Choose your shape:")
# shape_label.grid(row=0,column=0,padx=10,pady=5)

# shapes = ["circle", "square", "rect"]
# shape_var = StringVar()
# shape_drowp = OptionMenu(frame,shape_var,*shapes)
# shape_var.set(shapes[0])
# shape_drowp.grid(row=0,column=1,padx=10,pady=5)

# # Circle
# Radius = Label(frame,text="Radius: ")
# Radius.grid(row=1,column=0,padx=10,pady=5)
# Rentry = Entry(frame)
# Rentry.grid(row=1,column=1,padx=10,pady=5)

# # Square
# Side = Label(frame,text="Side: ")
# Side.grid(row=2,column=0,padx=10,pady=5)
# Sentry = Entry(frame)
# Sentry.grid(row=2,column=1,padx=10,pady=5)

# # Rect
# Length = Label(frame,text="Length: ")
# Length.grid(row=3,column=0,padx=10,pady=5)
# Lentry = Entry(frame)
# Lentry.grid(row=3,column=1,padx=10,pady=5)

# Width = Label(frame,text="Width: ")
# Width.grid(row=4,column=0,padx=10,pady=5)
# Wentry = Entry(frame)
# Wentry.grid(row=4,column=1,padx=10,pady=5)

# calculate = Button(frame,text="Calculate Area",command=calculate_area)
# calculate.grid(row=5,column=0,columnspan=2,pady=10)

# result = Label(main,text="",font=("Helvetica",20))
# result.pack(pady=20)

# main.mainloop()