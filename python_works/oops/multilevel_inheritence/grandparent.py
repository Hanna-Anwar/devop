class GrandParent:

    def house(self):

        print("grand parent house")


class Parent(GrandParent):

    def car(self):

        print("parent car")

class Child(Parent):

    def bike(self):

        print(" Child Bike")


child_instance = Child()

child_instance.bike()

child_instance.car()

child_instance.house()
