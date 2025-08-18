#  q3

# arr=[10,11,12,13,11,10,14]
# display duplicate number without any methods and 'in' operator

   #  0 1  2  3   4  5  6  7
arr=[10,11,12,13,11,10,14,14]

length = len(arr)

print(length)

for i in range(0,length): #[0,1,2,3,4,5,6,7] i=0 i=1 

    for j in range(i+1,length): #(1,7)[1,2,3,4,5,6] j=1 j=2 j=3 j=4 j=5.... j=2 j=3 j=4

        if arr[i]==arr[j]: #arr[0] 10==11  10==12  10==13 10==11 10==10... arr[1] 11 ==12 11==13  11==11

             print(arr[i]) #10 11

             break 