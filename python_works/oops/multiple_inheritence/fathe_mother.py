class Father:

    def cricket_skill(self):

        print("has cricket skill")

class Mother:

    def cooking_skill(self):

        print("has cooking skill")

class Child(Mother,Father): # multiple Inheritence

    def learning_skill(self):

        print("has learning skill")


child_instance = Child()

child_instance.learning_skill()

child_instance.cooking_skill()

child_instance.cricket_skill()