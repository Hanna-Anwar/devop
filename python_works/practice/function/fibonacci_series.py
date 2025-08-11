def fibo(limit):

  n1 = 0

  n2 = 1


  for i in range(1,limit+1):

        print(n1,end=",") #n1=0 1

        n3 = n1 +n2 #n3=1

        n1 = n2#n1=1

        n2 = n3#n2=1


limit = int(input("enter the limit : "))

fibo(limit)