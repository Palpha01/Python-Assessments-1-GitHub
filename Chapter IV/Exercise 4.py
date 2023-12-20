# Exercise 4: Letter count

# Develop a GUI App that asks the user to enter a character
# reads the contents of the sentences.txt file
# and counts the occurrences of the letter.

import tkinter
from tkinter import *
from tkinter import messagebox

def counting_letter_occurences(letter,content):
    return content.lower().count(letter.lower())

def read_file(mail_path):
    try:
        with open(mail_path,'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def show_letter_count():
    letter = mail.get()
    if not letter:
        messagebox.showinfo("Error", "Where is the letter for your mail?")
        return

    file_content = read_file('Python-Assessments-1-GitHub/Chapter IV/Texts/Sentences.txt')
    
    if file_content is None:
        messagebox.showinfo("Error", "File 'Python-Assessments-1-GitHub/Chapter IV/Texts/Sentences.txt' is not found.")
    
    occurences = counting_letter_occurences(letter,file_content)
    resultabel.config(text=f"Occurences of '{letter}': {occurences}")

app = Tk()
app.title("Exercise 4")

mailabel = Label(app,text="Enter a letter from the mail:")
mail = Entry(app)
submitton = Button(app,text="Count",command=show_letter_count)
resultabel = Label(app,text="")

mailabel.grid(row=0,column=0,padx=30,pady=30)
mail.grid(row=0,column=1,padx=30,pady=30)
submitton.grid(row=1,column=0,padx=30,pady=30)
resultabel.grid(row=2,column=0,padx=30,pady=30)

app.mainloop()