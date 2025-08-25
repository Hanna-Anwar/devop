text = "this is a python program to find most reursive word this python program is simple"

#display most frequent word

word_count = {}

sp = text.split(" ")

for word in sp:

    if word in word_count:

        word_count[word] +=1
 
    else:

        word_count[word] = 1

print(word_count)

#method 1

# sorting dict wrt values

srt_wc = sorted(word_count,reverse =True,key=word_count.get)

print(srt_wc)

#method 2

max_value =max(word_count.values())

for k,v in word_count.items():

    if v== max_value:

        print(k,v)