num = int(input("enter a number :"))

temp = num

rev = 0

while num != 0 :

  digit = num % 10

  rev =( rev * 10) + digit

  num //= 10


if temp == rev :
  
  print(f"{temp} is pallindrome ")

else:
  
 print(f"{temp} is not a pallindrome ")
   