#create a function is_prime with one parameter num return True if number is prime else  return false

# not include 1 and that no itself

def is_prime(num):

    is_prime = True    #T

    for i in range(2,num):#i=2  [2,3,4,5,6,7,8,9,10]

        if num % i == 0:  # 11%2 !=0

            is_prime = False

            break


    result = "prime" if is_prime == True else "not prime" #so execute this 
        
    print(result) 
    
is_prime(11)




