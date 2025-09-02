class Arg:

 def add(self,*args):

    print (sum(args))


arg_instance = Arg()

arg_instance.add(10,20,100)

#example method overloading

class Calculator:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

    def add(self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)#only this method works because python is interpreted 


cal_instance = Calculator()

cal_instance.add(10,20,30)

             
