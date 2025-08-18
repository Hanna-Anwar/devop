arr1 = [100,11,20,17,18]

arr2 = [10,20,17,12,18,9]

for num1 in arr1:

    for num in arr2:

        if num1==num:

            print(num)

print("****")

for num in arr1:

    if num in arr2:

        print(num)

print("****")


for num in arr1:

    if arr2.count(num) >0: # count of 100 in arr2 0

        print(num)

