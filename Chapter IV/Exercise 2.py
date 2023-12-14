# Exercise 2: CountString

# The file sentences.txt has a list of string data. Develop a GUI app that finds out how many times the following string appears

# Hello my name is Peter Parker
# I love Python Programming
# Love
# Enemy  

import tkinter

from tkinter import *

def count_occurences():
    string = entry.get()
    with open("Sentences.txt", 'r') as file:
        content = file.read()
        count = content.count(string)
        result.config(text="The string " + string + " appears " + count + " times.")

main = Tk()
main.title("Exercise 2")

entry = Entry(main, width=30).pack(pady=10)
search = Button(main, text="Search", command=count_occurences).pack()

result = Label(main, text="").pack(pady=10)

main.mainloop()