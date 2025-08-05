

num1 = int(input("enter number1 :")) #12
num2 = int(input("enter number2 :")) #14

while num2 != 0:       # 14!=0     8!=0      6!=0     2!=0

    temp = num1 % num2 # 12%14=8   14%8=6    8%6=2    6%2=0
 
    num1 = num2        #num1=14    num1=8    num1=6  **num1=2**

    num2 =temp         #num2=8     num2=6    num2=2   num2=0

print(num1)
