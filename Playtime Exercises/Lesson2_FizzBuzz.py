# Create a program that loops through the numbers 0-100.
# When you land on a number evenly divisible by 3, have your program print "Fizz"
# When you land on a number evenly divisible by 5, have your program print "Buzz"
# When you land on a number evenly divisible by both 3 and 5, have your program print "Fizzbuzz"
# When you land on any other number, print that number


for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print "Fizzbuzz"
    elif n % 3 == 0:
        print "Fizz"
    elif n % 5 == 0:
        print "Buzz"
    else:
        print n
