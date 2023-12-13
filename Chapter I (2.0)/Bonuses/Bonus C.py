# Exercise C: Calculator Function

# The program should display the following calculator menu:
# Add +, Subtract -, Multiply *, Divide /, Modulus %

# This adds two numbers

def add(a, b):
    return a + b

# This subtracts two numbers

def subtract(a, b):
    return a - b

# This multiplies two numbers

def multiply(a, b):
    return a * b

# This divides two numbers

def divide(a, b):
    return a / b

# This modulates two numbers

def modulus(a, b):
    return a % b

print("Choose your operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulate")

while True:
    choice = input("Selecting choice(1/2/3/4/5): ")
    
    if choice in ('1', '2', '3', '4', '5'):
        try:
            a = float(input("Enter your first number: "))
            b = float(input("Enter your second number: "))
        except ValueError:
            print("Sorry, wrong input")
            continue
        
        if choice == '1':
            print(a, "+", b, "=", add(a, b))    
        if choice == '2':
            print(a, "-", b, "=", subtract(a, b))
        if choice == '3':
            print(a, "*", b, "=", multiply(a, b))
        if choice == '4':
            print(a, "/", b, "=", divide(a, b))
        if choice == '5':
            print(a, "%", b, "=", modulus(a, b))
    break