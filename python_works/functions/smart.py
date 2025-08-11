
def smart_div(num1=10,num2=5):

    return num1-num2

# print(smart_div())

print(smart_div(100,80))
 
 
#create a function exponent with 2 param base and power

def exponent(base,power=1):   # if power is not passed as argument then we set it in parameter power =1 which will give 2**1

    return base ** power

print(exponent(2,3))