# Exercise 1: Woof Woof
# Develop a GUI using Tkinter with a class that defines the characteristics of a dog. The program should instantiate two objects from this class and assign data to its members. The program should then output the data from each object and the oldest dog should woof via a class method.

import tkinter as tk

from tkinter import*

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def woof(self):
        return f"{self.name},says woof"
dog1=Dog("German Shephard",10)
dog2=Dog("Husky",8)
older_dog=dog1 if dog1.age>dog2.age else dog2

class DogGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dog Info")
        self.geometry("400x400")
        self.display_dog_info()
        
    def display_dog_info(self):
        label1 = Tk.Label(self, "Dog1: {dog1.name},{dog1.age} years old")
        label1.pack()
        label2 = Tk.Label(self, "Dog2: {dog2.name},{dog2.age} years old")
        label2.pack()
        older_dog_label = Tk.label(self, text=f"the older dog is {older_dog.name}")
        older_dog_label.pack()
        woof_button = Tk.button(self, text="make woof")
        woof_button.pack()
        def woof (self):
            result=older_dog.woof()
            woof_label=Tk.Label(self,text=result)
            woof_label.pack()
    
app=DogGUI()
app.mainloop()