num1 = int(input("enter num1 :"))

num2 = int(input("enter num2 :"))


try:

    div_res = num1 / num2

    print("division = ",div_res)


except Exception as e:

    num2 = int(input("enter a number2 that is not 0 :"))

    div_res = num1/num2

    print(div_res)


finally:

    print("send text messege to user mobile phone")

    print("send email confirmation")

