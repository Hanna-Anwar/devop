# given an array of numbers find the closest number to zero
arr = [-2,-3,-4,-1,2,3,4,5,1]

closest_number =arr[0]

for num in arr:#-2

    if abs(num) < abs(closest_number): #abs(-2) <abs(-2) 2<2

        closest_number = num #closest_no = -2   

if  closest_number < 0 and abs(closest_number) in arr:


    closest_number = abs(closest_number)

print(closest_number)


