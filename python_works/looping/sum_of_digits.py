sum = 0

number = int(input("enter a number :")) #123 

while number!=0 : #123!=0 |   12!=0 | 1!=0| 0!=0

    digit = number % 10 # 123%10=3 | 12%10=2 | 1%10=1 

    sum += digit #0=0+3=3 | 3+2=5 | 5+1=6

    number //= 10 # 123//10=12 | 12//10=1 | 1//10=0

print(sum)