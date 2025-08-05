# 5. Count Even and Odd Digits in a Number
#  Write a program to count the number of even and odd digits in a given integer.
#   Example: 123456 -> Even: 3, Odd: 3


number = int(input("enter a number :"))

even_count = 0

odd_count = 0

while number != 0:

    digits = number % 10

    if  digits % 2 == 0:

        even_count += 1

    else:
        odd_count += 1

    number //= 10

print("even no count",even_count)
print("odd no count",odd_count)