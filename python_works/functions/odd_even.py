
#odd or even using fuction 

def odd_even(num):

    return f"{num} is even" if num %2==0 else f"{num} is odd"  #ternary operator

print(odd_even(16))



def last_digit_max(num1,num2):

    # number1 = num1 % 10 

    # number2 = num2 % 10

    # if number1 > number2: 

     return f"{num1} is large " if num1 % 10 > num2 % 10 else f"{num2} is large"
 
    # else :

    #      return f"{num2} is large"
    
    
print(last_digit_max(123,145))



