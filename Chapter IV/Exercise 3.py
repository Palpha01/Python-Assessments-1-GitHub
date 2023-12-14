# Exercise 3: Reading to a List

# The file numbers.txt has a list of 100 integer numbers each on a newline
# Create a python program that puts this data into a list, then output the values in integer format

with open("https://gist.github.com/miku/296a39fedea17ea448df9b10abdfcc9e=numbers.txt", "r") as file:
    numbers = [int(number) for number in file.readline()]
    
    for number in numbers:
        print(number)