def sum_n(num):#5

    if num == 0:

        return 0
    
    return num+sum_n(num-1)#0+sum_n(4)

print(sum_n(6))  