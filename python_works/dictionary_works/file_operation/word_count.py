""" Task 3: Count Each Word in a File
 Question:
 Create a file called words.txt containing a list of words separated by spaces. Write a program to
 read the content and display the count of each word in the file."""


file_path ="C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\words1.txt"

fr = open(file_path,"r")

w =[]

for line in fr:

   words = line.split()

   w.append(words)

print(w)

dict ={}

for word_list in w: 

    for word in word_list:

     if word not in dict:

        dict[word] =1

    else:

        dict[word]+=1

print(dict)