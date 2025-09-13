def sum_of_digit(num):

   if num == 0:

     return 0
       
   return num%10+sum_of_digit(num//10) #3+sum_of_digit(123//10),2+sum_of_digit(12//10),1+sum_of_digit(1//10)

print(sum_of_digit(123))