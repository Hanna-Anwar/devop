#exclude 1 and the number because it already a divisor 


# read number
# set is_prime as True
# Loop
#     check no is divisor


num = int(input("enter a number: ")) #4

is_prime = True

for i in range(2,num):        #[2,3] 2

    if num % i == 0:          #4%2==0

        is_prime = False      #is_prime =False

        break                 #break

result = "prime number" if is_prime == True else "not prime"

print(result)

# if  is_prime == True:

#     print(num,"is prime")

# else:

#     print(num,"is not prime")