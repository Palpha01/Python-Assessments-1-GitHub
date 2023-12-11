# Exercise 1: User input output

# Write code to prompt the user to input her/his name and age and print these details on the screen. Find the length of the name and also the age of the user after one year.

# Let's import the string first
import string

# Then we would take input from user
name = input("Hello, user! What is your name?: ")
age = int(input("What is your age?: "))

# Then we add one in the input and find the length of the name
age = age + 1
length = len(name)

# Finally, we print to see the results
print("It's good to meet you, " + name)
print("The length of your name is: "+ str(length))
print("You will be "+str(age)+" in a year")