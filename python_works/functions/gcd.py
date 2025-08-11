#create a function gcd with 2 param num1 num2 
#return gcd of num1 and0 num2


def gcd(num1,num2):

    limit = min(num1,num2)

    for i in range(2,limit+1):

        if num1 % i == 0 and num2 % i == 0 :

            gcd = i
    
    print(gcd)

gcd(6,12)