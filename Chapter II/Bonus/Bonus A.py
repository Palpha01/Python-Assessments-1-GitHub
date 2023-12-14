# Exercise A: Temperature Converter

# Develop a GUI that implements a temperature converter application using Tkinter, allowing users to convert between Celcius and Fahrenheit

import tkinter

from tkinter import *

from tkinter import messagebox

from functools import partial

temp_Val = "Celsius"

def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp

def call_convert(rlabel1,inputn):
    temp = inputn.get()
    
    if temp_Val == 'Celsius':
    
        f = float((float(temp) * 9 / 5) + 32)
        rlabel1.config(text ="%.1f Fahrenheit" % f)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Fahrenheit ", )
    
    if temp_Val == 'Fahrenheit':
    
        c = float((float(temp) - 32) * 5 / 9)
        rlabel1.config(text ="%.1f Celsius" % c)
        messagebox.showinfo("Temperature Converter", 
                            "Successfully converted to Celsius ")
    return

main = Tk()

main.geometry('500x500')

main.title('Temperature Converter')

main.grid_columnconfigure(1, weight = 1)
main.grid_rowconfigure(1, weight = 1)

Ninput = StringVar()
var = StringVar()

Linput = Label(main,text="Enter temperature")
Einput = Entry(main,textvariable=Ninput)
Linput.grid(row=1)
Einput.grid(row=1,column=1)
Rabel = Label(main)
Rabel.grid(row=3,columnspan=4)

drowplist = ["Celsius", "Fahrenheit"]
drowp = OptionMenu(main,var,*drowplist,
                        command = store_temp)
var.set(drowplist[0])
drowp.grid(row = 1, column = 2)

call_convert = partial(call_convert, Rabel,
                    Ninput)
Besult = Button(main, text ="Convert",
                        command = call_convert)
Besult.grid(row = 2, columnspan = 2)

main.mainloop()