def abs_dec(fun):

    def wrapper(num1,num2):

        return fun(abs(num1),abs(num2))
    
    return wrapper


@abs_dec
def add_numbers(num1,num2):

    return num1 + num2

print(add_numbers(-10,-10))