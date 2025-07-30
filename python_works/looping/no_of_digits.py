
# set number
# set count as 0 
# Loop
#    extract last
#    increment count by 1
#    remove last last_digit
# display count




number = int(input("enter a number :"))

count = 0

while(number != 0):

    last_digit = number % 10 #3

    count+=1 #0+1

    number//=10 #123//10=12

print(count)

