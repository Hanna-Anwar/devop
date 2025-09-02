class Shape:

    def __init__(self,name,edge_count):

        self.name = name

        self.edge_count = edge_count

    def calculate_area(self):

        print(f"calculating {self.name} area")


class Square(Shape):

    def __init__(self,name,edge_count,s):

        super().__init__(name,edge_count)

        self.s = s

    def calculate_area(self):
    
         area = self.s**2

         print(f"area of {self.name} is {area}")



#method 2 ******************************************************** 

class Rectangle(Shape):

    def __init__(self, name, edge_count):

        super().__init__(name, edge_count)

        
    def calculate_area(self,b,h):

        area = b * h

        print(f"area of {self.name} is {area}")

square_instance = Square("SQUARE",4,3)

square_instance.calculate_area()

rectangle_instance = Rectangle("RECTANGLE",4)

rectangle_instance.calculate_area(6,3)