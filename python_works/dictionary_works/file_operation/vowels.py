"""  Task 2: Display Words Starting with Vowels
 Question:
 Create a file called words.txt containing a list of words. Write a program to read the words from the
 file and display only the words that start with a vowel (a, e, i, o, u)"""



file_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\words.txt"

fr = open(file_path,"r")

vowel = "aeiou"

for word in fr:

    if word[0] in vowel:

        print(word)