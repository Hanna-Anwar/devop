# 9. Sum of All Digits in a Number
#  Take an integer input and calculate the sum of all its digits using a while loop.
#  Example:123 -> 1 + 2 + 3 = 6


number = int(input("enter a number :"))

sum = 0

while number!= 0:

    last_digit = number % 10

    sum+=last_digit

    number //= 10

print(sum)
