
# 1. Sum of Digits Until Single Digit
#  Write a program that repeatedly sums the digits of a number until a single-digit result is obtained.
#  Example: 987 -> 9+8+7=24 -> 2+4=6


num = int(input("enter number:"))

while num >= 10:

 sum = 0
 
 while num != 0 :

    digit = num % 10

    sum += digit

    num //= 10

 num = sum

print(" digit sum is:", num)   
