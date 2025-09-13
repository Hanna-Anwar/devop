# age = int(input("enter age :"))

# if age < 18:

#     raise Exception("Invalid age")


# o/p Exception: Invalid age



def divide(num1,num2):

    if num2 == 0:

        raise Exception("num2 should not be Zero..")
    

    else:

        return num1/num2
    

# print(divide(10,0)) #Exception: num2 should not be Zero..

print(f"result ={divide(10,2)}")