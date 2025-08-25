arr =[3,4,5,6,7]

#cubes using comprehension

cubes_list = [num**3 for num in arr]

print(cubes_list)

#squares using comprehension

squares_list = [num**2 for num in arr]

print(squares_list)

#return fruit in uppercase using list comprehension

fruits = ["apple","orange","grapes"]

new_list = [item.upper() for item in fruits]

print(new_list)

#print odd no

odd_list = [num for num in arr if num % 2 != 0]

print(f"odd_list is {odd_list}")

even_list = [num for num in arr if num % 2==0]

print(f"even_list is {even_list}")

num_gt_five = [num for num in arr if num > 5]

print(num_gt_five)
