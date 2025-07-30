year = int(input("enter year :"))                                #2020 #2023 #2000
  
 # year % 100 == 0 for finding if the yr is a centuary year THEN for checking if it is leap or not year divisible by 400
 # year % 100 != 0 for finding if the yr is a  not a centuary year THEN for checking if  it is leap or not year divisible by 4

  # 1st bracket chcking century year is leap or not 
  # 2 nd bracket checking non century year is leap or not

if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):

    print(year,"is a leap year")

else:

    print(year,"is not a leap year")



