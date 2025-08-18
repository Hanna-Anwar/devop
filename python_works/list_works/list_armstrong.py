# q4 
# numbers=[151,152,153,1634,8891,345,678]  153 = 1**3+5**3+3**3 
# display armstrong numbers from list

numbers = [151,152,153,1634,8891,345,678]

for i in numbers: #151
  
  temp = i

  sum = 0

  length = len(str(i))

  while i != 0:

    last_digit =  i % 10

    sum += last_digit ** length

    i //= 10

  if sum == temp:
    
    print(sum)


num = int(input)

     

            


