import tkinter as tk

from tkinter import *

class Employee:
    def __int__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.age = ""

    def setData(self, name, position, salary, id):
        self.name = name
        self.position = position
        self.salary = salary 
        self.id = id

    def getData(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, ID: {self.id}"

class Employee_GUI(tk, tk):
    def __int__(self):
        super().__int__()
        self.title("Employees details")
        self.geometry("400*400")
        self.employees = []
        self.add_employee()

    def add_employee(self):
        for _ in range(5):
            name = input("Enter name: ")
            position = input("Enter the position: ")
            salary = float(input("Enter the salary: "))
            id = input("Enter ID: ")
        employee = Employee()
        employee.setData(name, position, salary, id)
        self.employee.append(employee)
        self.display.employees()

    def display_employees(self):
        for employee in self.employees:
            print(employee.getData())
app = Employee_GUI()
app.mainloop()