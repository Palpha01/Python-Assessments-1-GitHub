import tkinter
from tkinter import *
from tkinter import ttk

class ArithmeticOperations(Tk):
    def __init__(Palpha):
        super().__init__()
        Palpha.title("Exercise 6")
        Palpha.geometry("300x200")

        Palpha.result = 0

        Palpha.create_widgets()

    def create_widgets(Palpha):
        Palpha.operation_label = Label(Palpha,text="Select Operation: ")
        Palpha.operation_label.pack()

        Palpha.operations = ttk.Combobox(Palpha,values=["Addition","Subtraction","Multiplication","Division"])
        Palpha.operations.pack()

        Palpha.num1_label = Label(Palpha,text="Enter first number: ")
        Palpha.num1_label.pack()
        Palpha.num1_entry = Entry(Palpha)
        Palpha.num1_entry.pack()

        Palpha.num2_label = Label(Palpha,text="Enter second number: ")
        Palpha.num2_label.pack()
        Palpha.num2_entry = Entry(Palpha)
        Palpha.num2_entry.pack()

        Palpha.calculate_button = Button(Palpha,text="Calculate",command=Palpha.calculate)
        Palpha.calculate_button.pack()

        Palpha.result_label = Label(Palpha,text="")
        Palpha.result_label.pack()

    def calculate(Palpha):
        operation = Palpha.operations.get()
        num1 = float(Palpha.num1_entry.get())
        num2 = float(Palpha.num2_entry.get())

        if operation == "Addition":
            Palpha.result = num1 + num2
        elif operation == "Subtraction":
            Palpha.result = num1 - num2
        elif operation == "Multiplication":
            Palpha.result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                Palpha.result = num1 / num2
            else:
                Palpha.result = "Undefined (Division by zero)"

        Palpha.result_label.config(text=f"Result: {Palpha.result}")

app = ArithmeticOperations()
app.mainloop()