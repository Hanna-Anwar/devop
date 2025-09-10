def swap_decorator(func):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return func(n1,n2)
    
    return wrapper

@swap_decorator
def sub(n1,n2):

    return n1-n2

@swap_decorator
def div(n1,n2):

    return n1/n2

print(sub(5,10))

print(div(5,10))

