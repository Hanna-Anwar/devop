text = "flOwer".casefold()

vowel = "aeiou"

v_count = 0

# for ch in range(0,len(text)):

#     for v in range(0,len(vowel)):

#           if text[ch] == vowel[v]:
                    
#            v_count+=1

# print(f"vowel count is {v_count}")



for ch in text:

       if ch in vowel:

        v_count+=1

print(f"vowel count is {v_count}")






