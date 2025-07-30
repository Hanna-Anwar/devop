# if number  div by 3 print ping
# if number  div by 5 print pong
# if number  div by 15 print pingpong

num = int(input("enter number "))

if num % 15 == 0:

    print("PINGPONG")

elif num% 3 ==0:

    print("PING")

elif num % 5 == 0:

    print("PONG")