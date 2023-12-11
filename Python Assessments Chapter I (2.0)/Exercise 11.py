# Exercise 11: Year Tuples

# Create a tuple with values

year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

print(year)

# Access the value at index -3

print(year[-3])

# Reverse the tuple and print the original tuple and reversed tuple

r = reversed(year)
print(tuple(r))

# Count number of times 2009 is in the tuple (use count() method)

c = year.count(2009)
print(c)

# Get the index value of 2018(Use index method)

i = year.index(2018)
print(i)

# Find length of given tuple(Use len() method)

print(len(year))