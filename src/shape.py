class Shape:

    def area(self):
        pass

    def periMtr(self):
        pass

class Circle(Shape):

    def __init__(self,radius:float):
        self.radius = radius


    def area(self):
        return 3.14*self.radius**2
    
    def periMtr(self):
        return 6.28*self.radius


class Square(Shape):

    def __init__(self,side:float):
        self.side = side


    def area(self):
        return self.side**2
    
    def periMtr(self):
        return 4*self.side