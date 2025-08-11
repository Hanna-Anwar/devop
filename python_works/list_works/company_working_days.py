attendance = ["H","P","P","P","P","L","H","H","P","P","P","P","L","H"]

working_day= 0

leave = 0

for i in attendance: #i=h

    if i == "P" or i=="L":

        working_day +=1

print("total working days=",working_day)

for i in attendance:

    if i == "L":

        leave+=1

print("Leave =",leave)





