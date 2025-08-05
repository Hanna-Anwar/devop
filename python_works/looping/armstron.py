# 3. Check for Armstrong Number
#  Check whether a number is an Armstrong number using a while loop.
# Example: 153 -> 1^3 + 5^3 + 3^3 = 153

number = int(input("enter a number :"))



length = len(str(number))

sum = 0

temp = number

while  number != 0 :

    last_digit = number % 10

    exponent = last_digit ** length

    sum += exponent

    number //= 10


if sum == temp :

    print(temp,"is armstrong")

else :

    print(temp,"is not armstrong")





