# check number is divisible by  5,3,7

number = int(input("enter number :"))

result = number % 3 == 0 and number % 5 == 0 and number % 7 == 0

print(result)


# check number is divisible by  2,4,8

number = int(input("enter number "))

res = number % 2 == 0 and number % 4 == 0 and number % 8 == 0

print(res)