# 2. Reverse a Number
#  Take an integer input and print its reverse using a while loop.
#  Example: 1234 -> Output: 4321


number = int(input("enter a number :"))

reverse = 0

while number != 0:

    last_digit = number % 10

    reverse = (reverse * 10) + last_digit

    number //= 10

print(reverse)

