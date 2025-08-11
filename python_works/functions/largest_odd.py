# 2374
#4 chk 4 is odd
#237
#7 chk odd or not yes 

def max_odd_number(number):

    while(number != 0):

        digit =  number % 10

        if digit %2 != 0:

            print(number)

            break

        number//= 10

max_odd_number(1546981)




