# 4. Generate Fibonacci Series (Up to N Terms)
#  Use a while loop to generate and print the first n terms of the Fibonacci sequence

number = int(input("enter number of terms :"))

n1, n2 = 0,1

count = 0

while   count < number :
  
    print(n1,end=" ")

    n3 =  n1 + n2

    n1 = n2

    n2 = n3

    count+=1

  