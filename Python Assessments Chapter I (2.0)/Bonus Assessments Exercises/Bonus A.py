# Bonus A: Multiplication Tables

# Write a program to print Multiplication table in following format from 1 to 10 tables
# Hint: Use nested loops


# Multiplication table of 1
print ("Multiplication table of 1")
number = int(input("Enter an integer: "))

for count in range (1, 11):
    product = number * count
    print(number, "*", count, "=", product)
    
# Multiplication table of 10
print ("Multiplication table of 10")
number = int(input("Enter an integer: "))

for count in range (1, 11):
    product = number * count
    print(number, "*", count, "=", product)