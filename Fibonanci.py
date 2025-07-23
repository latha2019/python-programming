# Python program to print the first 12 "even" Fibonacci numbers
# Assume the first two Fibonacci numbers to be 1 and 1
first = 1
sec = 1
count = 1
print("The first 12 'even' Fibonacci numbers are:")
while count <= 12:
    third = first + sec
    if third % 2 == 0:
        print(third)
        count = count + 1

    first, sec = sec, third
