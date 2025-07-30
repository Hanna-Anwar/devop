# set number
# find digit count
# set sum  as 0 

# loop
#    extract last_digit
#    exponent
#   add exponent with sum
#   remove  last_digit

# display sum

number = 153

length= len(str(number))

sum = 0

while (number!=0): 

  last_digit = number % 10

  exponent = last_digit ** length

  sum += exponent

  number //=10

print(sum)
