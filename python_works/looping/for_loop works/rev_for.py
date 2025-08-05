# 5. Reverse a Number
# Input a number. Reverse it using a for loop and arithmetic (e.g., 123 -> 321).


num = int(input("enter a number "))

string = str(num)

rev =0

for i in range(0,len(string)):

    digits = num % 10

    rev = (rev * 10)+ digits

    num //= 10

print(rev)