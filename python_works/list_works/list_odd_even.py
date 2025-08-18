arr = [ 1,10,11,12,34,35]

new_arr_even = []

new_arr_odd = []

for num in arr:

    if num % 2 == 0:
    
       new_arr_even.append(num)


    else:

        new_arr_odd.append(num)
 
print(new_arr_even)
print(new_arr_odd)
