# q2
# arr=[1,2,4,5]
# find least +ve missing number.

arr=[ 1,2,3,4,5,7]
     #0 1 2 3 4 5
length= len(arr)#1,2,3,4,5,6 len = 6

print(length)

for i in range(0,length-1):#[0,1,2,3,4]

    j = i+1 

    dif = arr[j]-arr[i] 
   
    if dif != 1:
         
        print(f"missing no is {arr[i]+1}")

        break

   
