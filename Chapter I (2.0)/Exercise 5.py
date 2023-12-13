# Exercise 5: Continue

# Write a program that implements a while loop. This program should ask the user if they would like to continue and use the while loop to keep looping as long as they enter the letter Y. Once the while loop has terminated output the number of times it is executed.

# range() is vital for this one. Any destinative number that makes the limit will cause a continous loop until it reach it's destination before the targeted number
for Y in range(13):
    if Y == 10:
        continue
    print (Y)