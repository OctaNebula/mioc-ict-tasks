import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def plot(self):
        plt.plot(self.x, self.y, 'ro')
        plt.axis([0, 10, 0, 10])
        plt.show()

    def plotArray(self, p):
        plt.plot([self.x, p.x], [self.y, p.y], 'ro-')
        plt.axis([0, 10, 0, 10])
        plt.show()
p1 = Point(1, 2)
p2 = Point(4, 6)

print(p1.distance(p2))

p1.plotArray(p2)
