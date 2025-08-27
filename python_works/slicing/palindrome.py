arr=["word","madam","racecar","car"]

a=[]

for i in arr:

    if i[::-1] == i:

        a.append(i)

print(a)
        

#******************OR

pallindrome_word = [i for i in arr if i[::-1]==i]

print(pallindrome_word)


#*********************************Reversing the full array

reversed_arr = arr[::-1]

print(reversed_arr)
