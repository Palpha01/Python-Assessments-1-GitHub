# Exercise 8: Print Pattern

# Write a program to display the following pattern using nested loops.

# This one is interesting. We're making a pyramid using input() and range()
e = int (input("enter the number of rows:"))
for i in range (1, e+1):
    for j in range (1, i+1): 
        print (j, end="")
    print()