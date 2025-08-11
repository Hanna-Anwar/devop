# q5

# numbers =[11,12,13,33,131,343,12321,1234]

# display palindromic numbers from list

numbers =[11,12,13,33,131,343,12321,1234]

for i in numbers:

    rev = 0

    temp = i

    while i != 0:

        last_digit = i % 10

        rev = (rev * 10) + last_digit

        i //= 10

    if rev == temp:

        print(temp)