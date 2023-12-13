# Exercise B: Locations List

# Using the list:
locations = ['Dubai','Paris', 'Switzerland', 'London', 'Amsterdam', 'New York']

# Note: I'm pretty sure you could've used 'Bern' instead of 'Switzerland'

# Print the list and find the length of the list

l = len(locations)

print ("The length of your tour lists is: ", l)

# Use sorted() to print your list in alphabetical order without modifying the actual list.

s = sorted(locations)

print (s)

# Show that your list is still in its original order by printing it.

print (locations)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list

print(sorted(locations, reverse=True))

# Show that your list is still in its original order by printing it again.

print (locations)

# Use reverse() to change the order of your list.

locations.reverse()

# Print the list to show that its order has changed.

print(locations)

# Use sort() to change your list so it’s stored in alphabetical order.

locations.sort()

# Print the list to show that its order has been changed.

print(locations)

# Use sort() to change your list so it’s stored in reverse alphabetical order.

locations.sort(reverse=True)

# Print the list to show that its order has changed.


print(locations)