# Exercise 9: Integer list

# Create an integer list and perform following operations

# Create an int list with 10 values

ten = [50, 40, 30, 20, 10, 60, 70, 80, 90, 100]

# Output the list using 'a' for loop

for a in ten:
    print(a)

# Output the highest and lowest value

high = max(ten)
low = min(ten)
print ("The highest number is",high)
print ("The lowest number is",low)

# Sort the elements in ascending order

ascend = sorted(ten)
print ("This list is ascended", ascend)

# Sort the elements in descending order

ten.sort(reverse=True)
print ("This list is descended", ten)

# Append two elements (Note: This is my favorite part)

countries = ["Philippines, Ireland, Poland, Netherlands, United States"]
countries.append ("Japan")
countries.append ("Lithuania")

# Print the list after appending

print(countries)