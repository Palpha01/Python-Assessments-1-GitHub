# Exercise 2: Coffee Vending Machine

# Develop a coffee Vending Machine that asks users to select the type of coffee, and also prompts users to select various options like sugar, milk, etc. Once selected display the message using a message box. Also, use images in the app.  
# Extension: Add other features to the previous app such as handling money.

import tkinter

from tkinter import *

main = Tk()

main.title('Exercise 2')
main.geometry('500x500')

header = Label(main,text="Coffee Vending Machine",font=("Helvetica", 10, "bold"),width=60,bg='brown',bd=10,fg='white',relief=RAISED)
header.grid(row=0,column=0)

main.mainloop()