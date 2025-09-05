class Parent:

    def car(self):

        print("car")

    def bikes(self):

        print("bike2")

class child(Parent): #inheriting here

    def bikes(self):

        print("bike")

child_instance = child()

child_instance.bikes()

child_instance.car()