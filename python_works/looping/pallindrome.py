# 7. Check Palindrome Number
#  Determine whether a number is a palindrome (reads the same forward and backward) using a while loop.
#  Example: 121 -> Palindrome

number = int(input("enter a number "))


reverse = 0

temp = number

while(number != 0):


    last_digit = number % 10

    reverse = (reverse * 10) + last_digit

    number //= 10



if reverse == temp :

    print(reverse,"is pallindrome")

else :

    print(reverse,"not a pallindrome")
