#create a function is_pallindrome with 1 paramerter num 
# return T if num is palindrome else return F


def is_pallindrome(num): #121

    temp = num

    rev = 0

    while num != 0:  #121 !=0

        last_digit = num % 10  #121%10 =1

        rev = (rev * 10 )+last_digit #1

        num //= 10 #121//=10 12

    # if temp == rev:

    #     return True
    
    # else:

    #     return False
    
    return "True" if temp == rev else "False"

print(is_pallindrome(1251))
