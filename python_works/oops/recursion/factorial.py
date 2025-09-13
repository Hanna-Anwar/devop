# num =5

# fact =1

# for i in range(1,num+1):


#     fact = fact*i

# print(fact)


#recursive approach


def factorial(num):#5
    
    fact =1

    if num ==0: 

        return 1
    
    return num*factorial(num-1)

print(factorial(5))