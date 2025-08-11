text = input("enter a string :").casefold()

v_count = 0

c__count = 0

vowel = "aeiou"

for ch in text:  #hanna@anwar

    if ch in vowel:

        v_count+=1
    
    elif ch.isalpha():

        c__count+=1

print(f"vowel count is {v_count}")

print(f"consonent count is {c__count}")