# Python program to print the first 12 "even" Fibonacci numbers
# Assume the first two Fibonacci numbers to be 1 and 1
num1 = 1
num2 = 1
count = 1
print("The first 12 'even' Fibonacci numbers are:")
for i in range(0,50):
    num3 = num1 + num2
    # print(num3)
    if num3 % 2 == 0:
        print(num3,"\t")
        count = count + 1
    if count > 12:
        break
    num1 = num2
    num2 = num3
