
#random is a python file ,where randint function is defined  to randomly choose the no between the range we defined.

# random.py

#     def randint(start,stop)




from random import randint  # this is for importing randint function from random.py file

target = randint(1,10)   # (1,10)=>this is thr range

count = 0

while True:

    number = int(input("guess the number :"))


    if number == target:

        print("congratzz...")
   
        break

    count+=1

print("attempt made is ",count)


                                                                                                                                                                