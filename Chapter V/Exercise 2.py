# Exercise 2: Student Class 
# Develop a GUI using Tkinter to Create a class called Students

# The class should have the following members.Name (string), Mark1 (int), Mark2 (int), Mark3 (int) 
# The class should have the following methods calcGrade() - should return an average from the three marks.display()- should output the student name and calculated grade average
# Create one object using a constructor that contains parameters to initialize all of the variables
# Ask user to input the variable values using input() and pass the values to the second object

import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(Palpha,name,mark1,mark2,mark3):
        Palpha.name = name
        Palpha.mark1 = mark1
        Palpha.mark2 = mark2
        Palpha.mark3 = mark3

    def calc_grade(Palpha):
        average = (Palpha.mark1 + Palpha.mark2 + Palpha.mark3) / 3
        return round(average, 2)

class StudentGUI:
    def __init__(Palpha,score):
        Palpha.score = score
        Palpha.score.title("Exercise 2")

        tk.Label(score,text="Student Name:").pack()
        Palpha.name_entry = tk.Entry(score)
        Palpha.name_entry.pack()

        tk.Label(score,text="Mark 1:").pack()
        Palpha.mark1_entry = tk.Entry(score)
        Palpha.mark1_entry.pack()

        tk.Label(score,text="Mark 2:").pack()
        Palpha.mark2_entry = tk.Entry(score)
        Palpha.mark2_entry.pack()

        tk.Label(score,text="Mark 3:").pack()
        Palpha.mark3_entry = tk.Entry(score)
        Palpha.mark3_entry.pack()

        Palpha.display_button = tk.Button(score,text="Display Student Info",command=Palpha.display_student_info)
        Palpha.display_button.pack()

    def display_student_info(Palpha):
        name = Palpha.name_entry.get()
        mark1 = int(Palpha.mark1_entry.get())
        mark2 = int(Palpha.mark2_entry.get())
        mark3 = int(Palpha.mark3_entry.get())

        if name and mark1 and mark2 and mark3:
            student = Student(name,mark1,mark2,mark3)
            average_grade = student.calc_grade()
            message = f"Student Name: {student.name}\nAverage Grade: {average_grade}"
            messagebox.showinfo("Student Information",message)
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

if __name__ == "__main__":
    main = tk.Tk()
    app = StudentGUI(main)
    main.mainloop()