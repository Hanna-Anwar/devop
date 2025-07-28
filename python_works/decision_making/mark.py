
mark1 = int(input("enter mark1 out of 50  :"))
mark2 = int(input("enter mark2 out of 50 :"))
mark3 = int(input("enter mark3 out of 50 :"))

total_mark = mark1 + mark2 + mark3 

print("total mark is",total_mark)

if total_mark > 140:

    print("good")

elif total_mark > 130  and total_mark <= 140:

    print("average")

elif total_mark <= 130:

    print("poor") 