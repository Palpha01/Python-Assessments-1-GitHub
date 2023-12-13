# Exercise 2: Managing Layout

# B: Square Grid
# With the pack layout manager, Create the following labels inside the frames. A and B inside the left frame. C and D inside the right frame

import tkinter as tk

main = tk.Tk()

main.title('Exercise 2 b')

Frame1=tk.Frame(main).pack()
Frame2=tk.Frame(main).pack()

A = tk.Label(Frame1, text="A", fg='white', bg='indigo', relief='sunken', bd=5).pack()
B = tk.Label(Frame2, text="B", fg='indigo',bg='white', relief='raised', bd=5).pack()
C = tk.Label(Frame1, text="C", fg='indigo', bg='white', relief='sunken', bd=5).pack()
D = tk.Label(Frame2, text="D", fg='white', bg='indigo', relief='raised', bd=5).pack()

main.resizable(True,True)
main.mainloop()