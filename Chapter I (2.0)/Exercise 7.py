# Exercise 7: Even Numbers

# Write a program that prints the even numbers from 1 to 100.
# Hint: Use Continue Statement

# Like last time, range() is useful for this one. Making 101 the ending number from 1 all the way to 100
for i in range (1, 101):
    if i % 2 != 0:
        continue
    print(i)