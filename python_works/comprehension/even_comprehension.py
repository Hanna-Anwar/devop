
# Given a list of integers, create a new list that contains the squares of only the even numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: [4, 16, 36, 64, 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [num **2 for num in numbers if num%2==0]

print(result)

#For a list of numbers, create a new list. If the number is positive, add it as is. If it's negative, add its absolute value.
#Also, only include numbers with an absolute value greater than 5.
#numbers = [10, -12, 3, -7, 8, -2, 15]
# Expected output: [10, 12, 8, 15]

numbers = [10, -12, 3, -7, 8, -2, 15]

result = [num if num>0 else abs(num) for num in numbers if abs(num)>5]

print(result)

# 4. Function Application
# Given a list of strings, use a list comprehension to create a list of the lengths of each string, but only for strings that start with a vowel.
# words = ["apple", "banana", "orange", "igloo", "umbrella", "cat", "dog"]
# vowels = ('a', 'e', 'i', 'o', 'u')
#Expected output: [5, 6, 5, 7]  # (apple, orange, igloo, umbrella)


words = ["apple", "banana", "orange", "igloo", "umbrella", "cat", "dog"]

result = [len(w) for w in words if w[0].lower() in "aeiou"]

print(result)


#Simple Dictionary Creation
#Create a dictionary where the keys are numbers from 1 to 5 and the values are their cubes.
#Expected output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

new_dict={}

limit = int(input("enter a limit: "))

for i in range(1,limit+1):

     new_dict[i]=i**3

print(new_dict)

#Conditional Key-Value Pairs
# From a dictionary of student names and their grades, create a new dictionary containing only the students who passed (grade >= 60).
# grades = {'Alice': 85, 'Bob': 59, 'Charlie': 72, 'David': 45, 'Eve': 90}
# Expected output: {'Alice': 85, 'Charlie': 72, 'Eve': 90}

grades = {'Alice': 85, 'Bob': 59, 'Charlie': 72, 'David': 45, 'Eve': 90}

result = {name:grade for name,grade in grades.items() if grade>=60}

print(result)

# Unique Squares with Condition
# Find all unique squares of numbers in a list that are greater than 20.
# numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3] # Note duplicates
# Expected output: {16, 25, 36}  # (4^2=16, 5^2=25, 6^2=36)

numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3] 

new_list = set(numbers)

print(new_list)

result = {num **2 for num in new_list if num ** 2 >20 }

print(result)


# Finding Unique Characters
# Given a string, create a set containing all the vowels ('a', 'e', 'i', 'o', 'u') that are present in the string, in lowercase.
# sentence = "Hello, how are you today?"
# Expected output: {'a', 'e', 'o', 'u'}  # (Notice 'i' is missing, 'y' is not a vowel for this exercise)

sentence = "Hello, how are you today?"

new_set = set(sentence)

print(new_set)

result = [i for i in new_set if i.lower() in "aeiou"]

print(result)

# Dictionary with List Values
# Create a dictionary that maps each letter to the list of words in a phrase that start with that letter.
# phrase = "the quick brown fox jumps over the lazy dog"
# Expected output (order may vary):
# {'t': ['the'], 'q': ['quick'], 'b': ['brown'], 'f': ['fox'], 'j': ['jumps'], 'o': ['over'], 'l': ['lazy'], 'd': ['dog']}

phrase = "the quick brown fox jumps over the lazy dog"

dict ={}

result = phrase.split() #['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

print(result[0])

for w in result:

     if 