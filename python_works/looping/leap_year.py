# q6 => diaplay all leap years from 1879 to 2026

i = 1879

while(i <= 2026):

    if (i % 100 == 0 and i % 400 == 0) or (i % 100 != 0 and i % 4 == 0):

        print(i,end=" ")

    i+=1