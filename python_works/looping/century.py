# q4 => display all century years from 1879 to 2026

i = 1879

while(i<=2026):

    if(i % 100 == 0): #century yr condition

        print(i,end=" ")
    
    i+=1