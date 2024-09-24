import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.c)

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a.distance(self.b)) * (p - self.b.distance(self.c)) * (p - self.c.distance(self.a)))

    def is_equilateral(self):
        return self.a.distance(self.b) == self.b.distance(self.c) == self.c.distance(self.a)

    def is_isoceles(self):
        return self.a.distance(self.b) == self.b.distance(self.c) or self.b.distance(self.c) == self.c.distance(self.a) or self.c.distance(self.a) == self.a.distance(self.b)

    def is_irregular(self):
        return not self.is_equilateral() and not self.is_isoceles()


p1 = Point(0, 0)
p2 = Point(0, 1)
p3 = Point(1, 0)

t = Triangle(p1, p2, p3)

if t.is_equilateral():
    print("Equilateral")
elif t.is_isoceles():
    print("Isoceles")
else:
    print("Irregular")