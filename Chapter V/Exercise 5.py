# Exercise 5: Playing around in class ☑️

# Use this exercise to play around with creating and accessing class members and methods.
# Develop a GUI using Tkinter to Create a class called Animal

import tkinter as tk

class Animal:
    def __init__(Palpha,animal_type,name,color,age,weight,noise):
        Palpha.type = animal_type
        Palpha.name = name
        Palpha.color = color
        Palpha.age = age
        Palpha.weight = weight
        Palpha.noise = noise

    def say_hello(Palpha):
        return f"Hey guys! Here is {Palpha.name}, a {Palpha.color} {Palpha.type}!"

    def make_noise(Palpha):
        return f"{Palpha.name} says: {Palpha.noise}"

class AnimalGUI(tk.Tk):
    def __init__(Palpha):
        super().__init__()
        Palpha.title("Exercise 5")
        Palpha.geometry("400x400")

        Palpha.create_widgets()

    def create_widgets(Palpha):
        labels = ["Animal Type","Name","Color","Age","Weight","Noise"]
        entries = []

        for label in labels:
            new_label = tk.Label(Palpha, text=label + ":")
            new_label.pack()
            new_entry = tk.Entry(Palpha)
            new_entry.pack()
            entries.append(new_entry)

        button_create = tk.Button(Palpha, text="Create Animal", command=lambda: Palpha.create_animal(*[entry.get() for entry in entries]))
        button_create.pack()

        Palpha.result_label = tk.Label(Palpha, text="")
        Palpha.result_label.pack()

    def create_animal(Palpha,animal_type,name,color,age,weight,noise):
        try:
            age = int(age)
            weight = float(weight)
            animal = Animal(animal_type,name,color,age,weight,noise)

            result_text = animal.say_hello() + "\n" + animal.make_noise()
            Palpha.result_label.config(text=result_text)
        except ValueError:
            Palpha.result_label.config(text="Nope. Please enter a valid age and weight")

app = AnimalGUI()
app.mainloop()