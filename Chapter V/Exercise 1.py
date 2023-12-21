# Exercise 1: Woof Woof
# Develop a GUI using Tkinter with a class that defines the characteristics of a dog. The program should instantiate two objects from this class and assign data to its members. The program should then output the data from each object and the oldest dog should woof via a class method.

import tkinter as tk

class Dog:
    def __init__(Palpha, name, age):
        Palpha.name = name
        Palpha.age = age

    def woof(Palpha):
        return f"{Palpha.name} says woof"

dog1 = Dog("German Shephard", 10)
dog2 = Dog("Husky", 8)
older_dog = dog1 if dog1.age > dog2.age else dog2

class DogGUI(tk.Tk):
    def __init__(Palpha):
        super().__init__()
        Palpha.title("Dog Info")
        Palpha.geometry("400x400")
        Palpha.display_dog_info()
        
    def display_dog_info(Palpha):
        label1 = tk.Label(Palpha, text=f"Dog1: {dog1.name}, {dog1.age} years old")
        label1.pack()
        label2 = tk.Label(Palpha, text=f"Dog2: {dog2.name}, {dog2.age} years old")
        label2.pack()
        older_dog_label = tk.Label(Palpha, text=f"The older dog is {older_dog.name}")
        older_dog_label.pack()
        woof_button = tk.Button(Palpha, text="Make Woof", command=Palpha.make_woof)
        woof_button.pack()
        
    def make_woof(self):
        result = older_dog.woof()
        woof_label = tk.Label(self, text=result)
        woof_label.pack()

app = DogGUI()
app.mainloop()