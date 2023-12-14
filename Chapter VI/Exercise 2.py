# Exercise 2: Numpy Array

# For the array a = [20,23,82,40,32,15,67,52] print the output of following:
# find the indices of even numbers
# Sort the array
# Slice elements from index 3 to the end of the array
# Slice elements from index 0 to index 4
# print [32 15 67] using negative slicing

import math

import numpy as np

a = [20,23,82,40,32,15,67,52]

# Indicing
print("Before: " + str(a))

odd_i = []
even_i = []
for i in range(0, len(a)):
    if i % 2:
        even_i.append(a[i])
    else:
        odd_i.append(a[i])

a = odd_i + even_i

print("After: " + str(a))        


# Sorting
array = np.array(a)

print(np.sort(array))

# slicing 1
s1 = a[3:]

print(s1)

# slicing 2
s2 = a[0:5]

print(s2)

# negative slicing
negs = a[4:7]

print(negs)