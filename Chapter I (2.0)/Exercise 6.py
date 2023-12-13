# Exercise 6: FizzBuzz

# Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# fizzbuzz is just... oddly new to me
for fizzbuzz in range(101):
    # if I could tell... numbers that are multiplied by 3 are fizz
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print ("FizzBuzz")
        continue
    # Continuing... numbers that are multiplied by 5 are buzz
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    # And numbers that are both multiplied by 3 and 5, ex. 50, are fizzbuzz
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)