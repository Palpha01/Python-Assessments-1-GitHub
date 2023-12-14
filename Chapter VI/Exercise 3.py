# Exercise 3: Calculator

# Write a program that will display the calculator menu

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def greatest(a, b):
    if a>b:
        return a
    else: 
        return b

print("Choose your operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulate")
print("6. Greater than")

while True:
    choice = input("Selecting choice(1/2/3/4/5/6): ")
    
    if choice in ('1','2','3','4','5','6'):
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
        if choice == '6':
            print("The greatest number is ",greatest(a, b))
            
    break