
text = "goodmorning"

# wc = {}

# for ch in text:
  
#    if ch in wc:

#       wc[ch]+=1

#    else: 

#       wc[ch] =1

   
# print(wc)

char_count = {}
              
for ch in set(text):

   char_count[ch] = text.count(ch)

print(char_count) 

max_frequency = 0

max_frequency_dictionary = {}

for k,v in char_count.items():

   if v > max_frequency:

      max_frequency = v

      max_frequency_dictionary.clear()

      max_frequency_dictionary[k]=v

print(max_frequency_dictionary)   