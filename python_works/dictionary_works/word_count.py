text = "python is simple python is easy"

words = text.split(" ") #['python', 'is', 'simple', 'python', 'is', 'easy']

print(words)

wc = {} 

for w in words: #w=python is simple python

    if w in wc: #python|is|simple|python|is|easy in wc 

        wc[w]+=1 #wc[python]=2|wc[is]=2

    else:

        wc[w]=1  #python=1 |is=1 |simple=1|easy=1

print(wc)