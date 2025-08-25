arr =[2,3,4,6,8,10]

#generate new list  map num as num+1,if num>5 else num-1

new_list = [num+1 if num >5 else  num-1 for num in arr]

print(new_list)

#create a new list of words starting with vowels

words = ["apple","banana","carrot","drumstick","egg","fish"]

vowel_list =[item for item in words if item[0].lower() in "aeiou"]

print(vowel_list)

#print longest word from word 

new_list = max(words,key=len)

print(new_list)


#dictionery comprehension

word_dict ={w:len(w) for w in words}

print(word_dict)

#dictioney comprehension return squares

arr =[6,7,8,9,10]

new_dict = {num:num **2 for num in arr}

print(new_dict)

orders = ["tea","dosa","tea","ghee-roast","tea","coffee","tea","idly","dosa"]

order_count = {item:orders.count(item) for item in orders}

print(order_count)