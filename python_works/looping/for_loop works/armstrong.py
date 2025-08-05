# 6. Check Armstrong Number (3-digit only)
# Input a 3-digit number. Check if it is an Armstrong number using a for loop.


# 153 =1*3+5*3+3*3


number = int(input("enter a number ")) #153

temp = number  #temp = 153

string = str(number)  #"153"

sum = 0

for i in range(0,len(string)):  # "1 5 3" i=1
   

   last_digit = number % 10

   sum = sum + (last_digit ** 3) 

   number //= 10 
   

if temp == sum:
   
   print("armstrong")

else:
   
   print("not")

