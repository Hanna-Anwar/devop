class Student():

    id : int

    name : str

    course : str


    def set_student(self,id,name,course):

        self.id = id

        self.name = name

        self.course = course

    
    def display(self):

        print(self.id,self.name,self.course)


student_instance1 = Student()

student_instance1.set_student(100,"remya","ASE")

student_instance1.display()

