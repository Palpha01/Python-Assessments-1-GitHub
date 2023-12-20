# Exercise 1: User information

# Develop a GUI App to create a file called 'bio.txt' and write the following information to the file asking user to enter the values (Name, Age, & Hometown)
# Each piece of data should be on a new line. Once the data has been written to the file, read the data from the file and output the data

import tkinter
from tkinter import *
from tkinter import messagebox

class UserInfoApp:
    def __init__(Palpha,main):
        Palpha.main = main
        Palpha.main.title("Exercise 1")
        
        Palpha.create_input_fields()
        Palpha.create_submit_button()
        
    def create_input_fields(Palpha):
        fields = ["Name: ", "Age: ", "Hometown: "]
        Palpha.entries = {}
        for field in fields:
            Label(Palpha.main,text=field + ": ").pack()
            Palpha.entries[field] = Entry(Palpha.main)
            Palpha.entries[field].pack()
    
    def create_submit_button(Palpha):
        submitton = Button(Palpha.main,text="Submit",command=Palpha.write_and_read_info)
        submitton.pack()
        
    def write_and_read_info(Palpha):
        user_info = ""
        for field, entry in Palpha.entries.items():
            value = entry.get()
            user_info += "{field}: {value}"
            
        with open("Python-Assessments-1-GitHub/Chapter IV/Texts/Bio.txt",'w') as file:
            file.write(user_info)
        
        with open("Python-Assessments-1-GitHub/Chapter IV/Texts/Bio.txt",'r') as file:
            user_info = file.read()
            messagebox.showinfo("User Information",user_info)

if __name__ == "__main__":
    root = Tk()
    app = UserInfoApp(root)
    root.mainloop()