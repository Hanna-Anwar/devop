class Calculator:

    def operation(self,n1,n2,**Kwargs):# def operation(self,*args,**Kwargs):

          # print(args)

          # print(kwargs)

        if Kwargs.get("op")=="+":

            return n1 + n2  #or return args[0]+args[1]
        
        if Kwargs.get("op")=="-":


            return n1-n2 #or return args[0]-args[1]


calculator_instance = Calculator()       

print(calculator_instance.operation(10,20,op="+"))
print(calculator_instance.operation(100,80,op="-"))