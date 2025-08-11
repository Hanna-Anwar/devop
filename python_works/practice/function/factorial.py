def factorial(num):

    fact = 1

    for i in range(1,num+1):

        fact = fact * i

    return fact


num = int(input("enter a number: "))

result = factorial(num)

print(f"factorial of {num} is {result}")