# Exercise 3: Employee Class
# Develop a GUI using Tkinter to Create an employee class with the following members: name, age, id, salary

# Add the following methods: setData() - should allow employee data to be set via user input,getData()- should output employee data to the console
# Create a list of 5 employees. Ask the user to enter the details of 5 employees using the add_employee method and then display the output using the display_emloyee method as mentioned below Expected output

import tkinter as tk

from tkinter import *

class Employee:
    def __init__(Palpha):
        Palpha.name = ""
        Palpha.position = ""
        Palpha.salary = 0.0
        Palpha.id = ""

    def set_data(Palpha, name, position, salary, id):
        Palpha.name = name
        Palpha.position = position
        Palpha.salary = salary
        Palpha.id = id

    def get_data(Palpha):
        return f"Name: {Palpha.name}, Position: {Palpha.position}, Salary: {Palpha.salary}, ID: {Palpha.id}"

class EmployeeGUI(tk.Tk):
    def __init__(Palpha):
        super().__init__()
        Palpha.title("Exercise 3")
        Palpha.geometry("400x400")
        Palpha.employees = []
        Palpha.create_input_fields()
        Palpha.create_display_button()

    def create_input_fields(Palpha):
        Palpha.name_label = tk.Label(Palpha, text="Name:")
        Palpha.name_entry = tk.Entry(Palpha)
        Palpha.name_label.pack()
        Palpha.name_entry.pack()

        Palpha.position_label = tk.Label(Palpha, text="Position:")
        Palpha.position_entry = tk.Entry(Palpha)
        Palpha.position_label.pack()
        Palpha.position_entry.pack()

        Palpha.salary_label = tk.Label(Palpha, text="Salary:")
        Palpha.salary_entry = tk.Entry(Palpha)
        Palpha.salary_label.pack()
        Palpha.salary_entry.pack()

        Palpha.id_label = tk.Label(Palpha, text="ID:")
        Palpha.id_entry = tk.Entry(Palpha)
        Palpha.id_label.pack()
        Palpha.id_entry.pack()

    def create_display_button(Palpha):
        Palpha.display_button = tk.Button(Palpha, text="Add Employee", command=Palpha.add_employee)
        Palpha.display_button.pack()

    def add_employee(Palpha):
        name = Palpha.name_entry.get()
        position = Palpha.position_entry.get()
        salary = float(Palpha.salary_entry.get())
        id = Palpha.id_entry.get()

        employee = Employee()
        employee.set_data(name, position, salary, id)
        Palpha.employees.append(employee)
        Palpha.display_employees()

    def display_employees(Palpha):
        Palpha.display_frame = tk.Frame(Palpha)
        Palpha.display_frame.pack()

        for employee in Palpha.employees:
            employee_label = tk.Label(Palpha.display_frame, text=employee.get_data())
            employee_label.pack()

app = EmployeeGUI()
app.mainloop()