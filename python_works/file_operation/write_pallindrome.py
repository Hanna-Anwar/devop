file_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\word.txt"

fw = open(file_path,"w")

words = ["hello","hai","racecar","madam","pangram"]

for w in words:

    if w[::-1] == w:

        fw.write(w +"\n")