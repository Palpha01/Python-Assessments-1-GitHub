# Exercise 4: Shapes

# Develop a GUI using Tkinter to calculate the area of Shapes. Create a parent class called Shape.
# This should have the following methods inputSides() – Ask the user to enter the sides of the shape.
# Now create subclasses for a circle, rectangle, and triangle.
# These should include an appropriate  area() method that will use the side values from the shape class.

import tkinter as tk
import math

class Shape:
    def __init__(Palpha,shaper):
        Palpha.shaper = shaper

    def input_sides(Palpha):
        Palpha.sideabel = tk.Label(Palpha.shaper,text="Enter sides:")
        Palpha.sideabel.pack()
    
    def input_radius(Palpha):
        Palpha.radiabel = tk.Label(Palpha.shaper,text="Enter radius:")
        Palpha.radiabel.pack()

class Circle(Shape):
    def __init__(Palpha,shaper):
        super().__init__(shaper)
        Palpha.input_radius()
        Palpha.radientry = tk.Entry(Palpha.shaper)
        Palpha.radientry.pack()
        Palpha.calculate = tk.Button(Palpha.shaper,text="Calculate Area",command=Palpha.calculate_area)
        Palpha.calculate.pack()

    def calculate_area(Palpha):
        radius = float(Palpha.radientry.get())
        area = math.pi * (radius ** 2)
        resultabel = tk.Label(Palpha.shaper,text=f"Area of the circle: {area}")
        resultabel.pack()

class Rectangle(Shape):
    def __init__(Palpha,shaper):
        super().__init__(shaper)
        Palpha.input_sides()
        Palpha.lengthentry = tk.Entry(Palpha.shaper)
        Palpha.lengthentry.pack()
        Palpha.widthentry = tk.Entry(Palpha.shaper)
        Palpha.widthentry.pack()
        Palpha.calculate = tk.Button(Palpha.shaper,text="Calculate Area",command=Palpha.calculate_area)
        Palpha.calculate.pack()

    def calculate_area(Palpha):
        length = float(Palpha.lengthentry.get())
        width = float(Palpha.widthentry.get())
        area = length * width
        resultabel = tk.Label(Palpha.shaper,text=f"Area of the rectangle: {area}")
        resultabel.pack()

class Triangle(Shape):
    def __init__(Palpha,shaper):
        super().__init__(shaper)
        Palpha.input_sides()
        Palpha.basentry = tk.Entry(Palpha.shaper)
        Palpha.basentry.pack()
        Palpha.heightentry = tk.Entry(Palpha.shaper)
        Palpha.heightentry.pack()
        Palpha.calculate = tk.Button(Palpha.shaper, text="Calculate Area", command=Palpha.calculate_area)
        Palpha.calculate.pack()

    def calculate_area(Palpha):
        base = float(Palpha.basentry.get())
        height = float(Palpha.heightentry.get())
        area = 0.5 * base * height
        resultabel = tk.Label(Palpha.shaper, text=f"Area of the triangle: {area}")
        resultabel.pack()

main = tk.Tk()
main.title("Exercise 4")

circleframe = tk.Frame(main)
circleframe.pack(side=tk.LEFT)
circlelabel = tk.Label(circleframe, text="Circle")
circlelabel.pack()
circle = Circle(circleframe)

rectangleframe = tk.Frame(main)
rectangleframe.pack(side=tk.LEFT)
rectanglelabel = tk.Label(rectangleframe, text="Rectangle")
rectanglelabel.pack()
rectangle = Rectangle(rectangleframe)

triangleframe = tk.Frame(main)
triangleframe.pack(side=tk.LEFT)
trianglelabel = tk.Label(triangleframe, text="Triangle")
trianglelabel.pack()
triangle = Triangle(triangleframe)

main.mainloop()