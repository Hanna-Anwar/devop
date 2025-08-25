numbers = [2,3,4,5,6]

dict = {}

for i in numbers:

    sq = i ** 2

    # dict[i] = sq
    
    dict.update({i:sq})

print(dict)