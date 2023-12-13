# Exercise 13: Product of list items

# Write a program that passes a list as an argument to a function. The function should then calculate the product (values multiplied) of the list values and return this value back to the main program.

# NumPy, as the name suggests, is for working with numbers in python, for operations like multiplication

import numpy

odd = [1, 3, 5]
even = [2, 4, 6]

result1 = numpy.prod(odd)
result2 = numpy.prod(even)

print(result1)
print(result2)
