m1 = int(input("enter mark1 out of 50: "))
m2 = int(input("enter mark2 out of 50: "))
m3 = int(input("enter mark3 out of 50: "))
m4 = int(input("enter mark4 out of 50: "))
m5 = int(input("enter mark5 out of 50: "))


avg_mark = (m1 + m2 + m3 + m4 + m5) / 5

if avg_mark <= 25:

    print("Fail")

elif 25 <avg_mark <= 30:

    print("D")

elif 30<avg_mark<=36:

    print("C")

elif 36< avg_mark<= 40:

    print("B")

elif 40 < avg_mark <=50:

    print("A")

else:

    print("Invalid")





