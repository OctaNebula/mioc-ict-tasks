import math

class GeometricalObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(GeometricalObject):
    def __init__(self, a, b):
        super().__init__(a, b)

    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
class Circle(GeometricalObject):
    def __init__(self, r):
        super().__init__(r, r)
    
    def area(self):
        return math.pi * self.a ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.a
    
class IrregularTriangle(GeometricalObject):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
    
    def area(self):
        return self.a ** 2
    
    def perimeter(self):
        return 4 * self.a
    
class RightTriangle(GeometricalObject):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.hypotenuse = math.sqrt((self.a)**2 + (self.b)**2)

    def area(self):
        return self.a * self.b / 2
    
    def perimeter(self):
        return self.a + self.b + self.hypotenuse
