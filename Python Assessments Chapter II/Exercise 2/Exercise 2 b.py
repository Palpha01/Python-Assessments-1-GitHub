# Exercise 2: Managing Layout

# B: Square Grid
# With the pack layout manager, Create the following labels inside the frames. A and B inside the left frame. C and D inside the right frame
# Using Pack() align A and C at the top and B and D at the bottom of the frames that contain them
# Support resizing. Use the ‘expand’ and ‘fill’ attributes of the pack method to make the labels grow and expand into the available space.
# Assign border value as 5 to the frames

import tkinter as tk

main = tk.Tk()

main.title('Exercise 2 b')

Frame1=tk.Frame(main).pack()
Frame2=tk.Frame(main).pack()

A = tk.Label(text="A", bg='indigo', relief=RAISED, bd=5).pack(side=TOP, expand=YES, fill=BOTH)
B = tk.Label(main, text="B", fg='white', relief=RAISED, bd=5).pack(side=BOTTOM, expand=YES, fill=BOTH)
C = tk.Label(main, text="C", bg='white', relief=SUNKEN, bd=5).pack(side=TOP, expand=YES, fill=BOTH)
D = tk.Label(main, text="D", fg='indigo', relief=SUNKEN, bd=5).pack(side=BOTTOM, expand=YES, fill=BOTH)

main.resizable(True,True)
main.mainloop()