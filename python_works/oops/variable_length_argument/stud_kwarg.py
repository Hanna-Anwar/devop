def stud_detail(**Kwargs):

    print(Kwargs)

    print(Kwargs["name"])


stud_detail(roll=1234,name="tom",place="london")