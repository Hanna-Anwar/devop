class Parent:

    def car(self):

        print("car")

    def bike(self):

        print("bike2")

class child(Parent): #inheriting here

    def bike(self):

        print("bike")

child_instance = child()

child_instance.bike()

child_instance.car()