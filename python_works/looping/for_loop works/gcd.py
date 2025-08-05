num1 = int(input("number1 :"))
num2 = int(input("number2 :"))

limit = min(num1,num2)

gcd = 1

for i in range(1,limit+1):

    if num1%i==0 and num2%i==0:

         gcd=i
  
print("gcd of 2 numbers are ",gcd)