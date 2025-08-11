# def vowel_consonent(word):

#     vowel_count = 0

#     consonent_count = 0

#     vowel = "aeiou"

#     for ch in word:

#      if ch in vowel:

#          vowel_count+=1


#     #  else:
         
    #      consonent_count+=1


   # print("vowel count",vowel_count)

    #print("consonent count",consonent_count)

 
#word = input("enter a string: ").casefold()

#vowel_consonent(word)



def vowel_consonent(word):#cat

    vowel_count = 0

    consonent_count = 0

    vowel = "aeiou"

    for i in range(0,len(word)):
         
         if word[i] in vowel:

             vowel_count+=1


         else:
         
             consonent_count+=1


    print("vowel count",vowel_count)

    print("consonent count",consonent_count)

 
word = input("enter a string: ").casefold()

vowel_consonent(word)