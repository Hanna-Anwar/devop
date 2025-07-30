#read year
#display century year if year ending with 00 zeroes
#else display non century year


year = int(input("enter year :"))

if year % 100 == 0:

    print(year,"is a century year")

else: 

    print(year,"is not a century year")