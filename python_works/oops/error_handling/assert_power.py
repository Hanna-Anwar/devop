def exponent(base,power):

    result = base ** power
    
    return result

assert exponent(5,2)==25 ,"test case1 failed"

assert exponent(2,3)==8 ,"test case2 failed"

assert exponent(2,0)==1 ,"test case3 failed with power as 0 "

print("completed")