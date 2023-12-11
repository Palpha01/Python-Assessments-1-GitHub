# Exercise 3: Is it a triangle

# Write a program that asks the user to enter the lengths of the three sides of a triangle. Use the triangle inequality to determine if we have a triangle
# Optional: If valid, ask the user for the length of the sides and have the program correctly classify the type of triangle as either: Equilateral, Isosceles or Scalene

# Let's make three inputs to measure the sides each
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

# Then we see if two sides are greater than one side using the if-else method, for we'll see the results
if a+b>c and b+c>a and c+a>b:
    
    # This should also identify what type of triangle is this 
    if a==b==c:
        print("This is an equilateral triangle.")
    elif a==b or b==c or c==a:
        print("This is an isosceles triangle")
    else:
        print ("This is a scalene triangle")
        
    # Otherwise, it's not even a triangle if typed something unexpected
else:
    print("Oof... this is not a triangle")