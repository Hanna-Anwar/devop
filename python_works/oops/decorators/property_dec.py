class Employee:

    def __init__(self,id,name,dept):

        self.id = id

        self.name = name

        self.dept = dept

    @property
    def get_name(self):

        print(self.nam e)


employee_instance = Employee(2,"jane","hr")

employee_instance.get_name #applied property decorator so no need of () becoz it will take get_name method as property not method

print(employee_instance.id)

print(employee_instance.dept)