import math

class Cuboid:
    def __init__(self, a, b, c):
        self.length = a
        self.width = b
        self.height = c

    def volume(self):
        return self.length * self.width * self.height
    
    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

class Cylinder:
    def __init__(self, h, r):
        self.radius = r
        self.height = h
    
    def volume(self):
        return round(math.pi * self.radius ** 2 * self.height, 2)
    
    def surface_area(self):
        return round(self.radius ** 2 * math.pi * 2 + 2 * math.pi * self.radius * self.height, 2)
    
class Cube(Cuboid):
    def __init__(self, a):
        super().__init__(a, a, a)

    def spatialDiagonal(self):
        return round(math.sqrt(3) * self.length, 2)

cuboid = Cuboid(2, 3, 4)
print(cuboid.surface_area())
print(cuboid.volume())

cylinder = Cylinder(7, 5)
print(cylinder.surface_area())
print(cylinder.volume())

cube = Cube(3)
print(cube.surface_area())
print(cube.volume())
print(cube.spatialDiagonal())
