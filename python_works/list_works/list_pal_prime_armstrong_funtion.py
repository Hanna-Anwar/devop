# q1
# arr=[153,151,1634,1771,2332]
# generate three new list palindrome_list and armstrong_list,prime_number



def pallindrome(arr):#arr=[153,151,1634,1771,2332]

    pallindrome_list = []


    for num in arr:#153

        rev = 0

        temp = num

        while num!=0:

            last_digits = num % 10

            rev = (rev * 10) + last_digits

            num //= 10

        if rev == temp:

            pallindrome_list.append(temp)

    return pallindrome_list

def armstrong(arr):

 armstrong_list = []

 for num in arr:
          
          length = len(str(num))

          sum = 0

          temp = num

          while num != 0 :
              
              last_digit =  num % 10

              sum += last_digit ** length

              num //= 10

          if sum == temp:
              
              armstrong_list.append(temp)
 
 return armstrong_list
  
def primeno(arr):

 prime_list = []

 for num in arr:

    is_prime = True

    for i in range(2,num):

         if num % i == 0:
             
             is_prime = False

             break
         
    if is_prime == True:
             
            prime_list.append(num)

            return prime_list

arr=[153,151,1634,1771,2332]

result1 = pallindrome(arr)

print(f"Pallindrome nos in the list are {result1}")

result2 = armstrong(arr)

print(f"armstrong nos in the list are {result2}")

result3 = primeno(arr)

print(f"prime nos in the list are {result3}")


# q3

# arr=[10,11,12,13,11,10,14]
# display duplicate number without any methods and 'in' operator