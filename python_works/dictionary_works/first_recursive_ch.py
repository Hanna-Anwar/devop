#text ="ABCABC"
# Display first recursive character


text = "ABCABB"

emd = {}

for ch in text:

    if ch in emd:

        print(ch)

        break

    else:

        emd[ch]=1