# Exercise 12: Area Functions

# Code a program to display a menu on the screen that asks if the user wants to

# Here we go again, this time with Math by importing pi

from math import pi

# Calculating the area of the Square

s = float(input("Enter the side length of the square: "))

area = s * 2

print("The area of the square is: ", area)

# Calculating the area of the Triangle

l = float(input("Enter the base length of the triangle: "))
h = float(input("Enter the base height of the triangle: "))

area = 0.5 * l * h

print("The area of the triangle is: ", area)

# Calculating the area of the Circle

r = float(input("Enter the area of the circle: "))

area = pi * r ** 2

print("The area of the circle with radius ", r , " is: ", area)