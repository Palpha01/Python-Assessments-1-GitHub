# Exercise 2: CountString

# The file sentences.txt has a list of string data.
# Develop a GUI app that finds out how many times the following string appears

# Hello my name is Peter Parker
# I love Python Programming
# Love
# Enemy

import tkinter
from tkinter import *

def count_string_occurrences():
    target_strings = [
        "Hello my name is Peter Parker",
        "I love Python Programming",
        "Love",
        "Enemy"
    ]

with open("Python-Assessments-1-GitHub/Chapter IV/Texts/Sentences.txt",'r') as file:
    data = file.read()
    
occurrences = [data.count(string) for string in target_strings]

result.config(text="Occurrences: {occurrences}")

main = Tk()
main.title("Exercise 2")

instructions = Label(main,text="Count the string occurrences in the file")
instructions.pack()

count = Button(main,text="Count Occurrences",command=count_string_occurrences)
count.pack()

result = Label(main,text="Occurrences: ")

main.mainloop()