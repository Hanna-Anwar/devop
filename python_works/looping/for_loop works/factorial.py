# write a program to find the factorial of a number
# 3=1*2*3

num = int(input("enter number: "))

factorial = 1

for i in range(1,num+1):

    factorial *= i

print(f"factorial of {num} = ",factorial)