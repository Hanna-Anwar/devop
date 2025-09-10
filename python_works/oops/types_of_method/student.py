class Student:

    school_name = "SNCS" #class varialble

    def __init__(self,rol,name,total):

        self.rol = rol

        self.name = name

        self.total = total

    @classmethod
    def update_school_name(cls,new_school_name):

        cls.school_name = new_school_name

        print(f"new school name is {cls.school_name}")

    @staticmethod
    def is_pass(total):

        return True if total>145 else False

Student.update_school_name("ST gregorious Public School")

student_instance1 = Student(100,"hanna",149)

student_instance2 = Student(128,"jiya",100)

print(Student.is_pass(student_instance1.total))

print(Student.is_pass(student_instance2.total))
    
      

      #OOPS END