# Exercise 4: Line graph 

# Draw a line in a diagram from position (1, 2) to position (6, 8)
# Draw a dotted line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)

import matplotlib.pyplot as plt

x = [1, 6]
y = [2, 8]

xdot = [1, 2, 6, 8]
ydot = [3, 8, 1, 10]

plt.plot(x, y)

plt.plot(xdot, ydot, linestyle='dotted')

plt.legend()

plt.show()