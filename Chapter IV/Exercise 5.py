# Exercise 5: Password Check
# Develop a GUI App to check the validity of a password given by the user in the entry widget
# The password should satisfy the following criteria:

# Contain at least 1 letter between a and z
# Contain at least 1 number between 0 and 9
# Contain at least 1 letter between A and Z
# Contain at least 1 character from $, #, @
# Minimum length of password: 6
# Maximum length of password: 12

# Ask user to include a maximum of 5 passcode attempts
# Each time the user enters an incorrect passcode, they should be prompted of how many passcode attempts remain
# If there are 5 failed passcode attempts the while loop should break and inform the user that the authorities have been alerted

import tkinter
from tkinter import *
from tkinter import messagebox
import re

def is_valid_password(password):
    if (6<=len(password)<=12 and
        re.search("[a-z]",password)and
        re.search("[0-9]",password)and
        re.search("[A-Z]",password)and
        re.search("[$#@]",password)):
        return True
    return False

def check_password():
    entered_password = pentry.get()
    
    if is_valid_password(entered_password):
        messagebox.showinfo("Valid","Access granted!")
    else:
        messagebox.showwarning("Invalid","Access denied.")

app = Tk()
app.title("Exercise 5")

pabel = Label(app,text="Enter your password: ")
pentry = Entry(app,show="*")
checkon = Button(app,text="Check",command=check_password)

pabel.pack(pady=10)
pentry.pack(pady=10)
checkon.pack(pady=10)

app.mainloop()