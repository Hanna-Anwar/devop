def pass_fail(m1,m2,m3):

    avg = (m1+m2+m3)/3

    if m1>35 and m2>35 and m3>35 and avg>=50:

        print("pass")

    else:

        print("fail")

m1 = int(input("enter m1: "))

m2 = int(input("enter m2: "))

m3 = int(input("enter m3: "))



pass_fail(m1,m2,m3)