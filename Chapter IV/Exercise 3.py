# Exercise 3: Reading to a List

# The file numbers.txt has a list of 100 integer numbers each on a newline
# Create a python program that puts this data into a list, then output the values in integer format

file = open("Python-Assessments-1-GitHub/Chapter IV/Numbers.txt","r")

print(file.read())