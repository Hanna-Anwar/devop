#write a program to chk given string is pangram


text = "The quick brown fox jumps over the lazy dog" .casefold()

alp = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for ch in alp:

    if ch not in text :

        is_pangram = False

        break

print(is_pangram)



