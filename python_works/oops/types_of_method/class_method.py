class Employee:

    def __init__(self,id,name):

        self.id = id

        self.name = name

    def display_employee(self): #instance method bound to object

        print(f"employee id = {self.id}\nemployee name = {self.name}")


    @classmethod
    def cls_method_demo(cls): #class method bound to class sf

        print("inside class method")



    @staticmethod
    def stat_method_demo():#static method

        print("inside statitic method")


emp_instance = Employee(1,"hanna")

emp_instance.display_employee()

Employee.cls_method_demo()

Employee.stat_method_demo()
        