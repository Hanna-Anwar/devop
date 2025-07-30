
# loop number !=0
# step1 extract last_digit= number % 10
# step2 floor_number =number // 10


number = int(input("enter a number : ") ) #123

while(number !=  0):      #123 !=0 12!=0 1!=0 0!=0

    last_digit = number % 10  #123%10=3 12%10=2 1%10=1
    
    print(last_digit)  #321

    number //= 10  #123//10=12 12//10=1 1//10=0

    