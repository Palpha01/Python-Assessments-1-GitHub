# Exercise 4: Largest number

# Write a program to input three numbers and outputs the largest using the multiple if -else statements

# Three inputs to insert three numbers
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# And just like the last time, we compare them using the if-else method
# this time with elif to see the results
if (a>b) and (a>c):
    print("a has the largest number.")
elif (b>a) and (b>c):
    print("b has the largest number.")
else:
    print("c has the largest number.")