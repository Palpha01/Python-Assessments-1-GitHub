# Exercise 2: Maths

# Write a program that evaluates the following calculations for two int numbers obtained from the user and outputs the results to the console:
# (Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%))

# Just like last time, let's import math first

import math

# Next we put the inputs for the user to type in

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

# Finally, we print to see the results

print("Sum: ",a+b)
print("Difference: ",a-b)
print("Product: ",a*b)
print("Quotient: ",a/b)
print("Remainder: ",a%b)