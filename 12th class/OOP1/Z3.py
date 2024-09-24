class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def is_parallel(self, l):
        return (self.p1.y - self.p2.y) * (l.p1.x - l.p2.x) == (self.p1.x - self.p2.x) * (l.p1.y - l.p2.y)

    def is_perpendicular(self, l):
        return (self.p1.y - self.p2.y) * (l.p1.y - l.p2.y) == -(self.p1.x - self.p2.x) * (l.p1.x - l.p2.x)

    def intersection(self, l):
        a1 = self.p2.y - self.p1.y
        b1 = self.p1.x - self.p2.x
        c1 = a1 * self.p1.x + b1 * self.p1.y

        a2 = l.p2.y - l.p1.y
        b2 = l.p1.x - l.p2.x
        c2 = a2 * l.p1.x + b2 * l.p1.y

        det = a1 * b2 - a2 * b1
        if det == 0:
            return None
        x = (b2 * c1 - b1 * c2) / det
        y = (a1 * c2 - a2 * c1) / det
        return Point(x, y)

# intersection example

l1 = Line(Point(1, 1), Point(2, 2))
l2 = Line(Point(1, 2), Point(2, 1))

print(l1.is_parallel(l2))
print(l1.is_perpendicular(l2))
print(l1.intersection(l2).x, l1.intersection(l2).y)

# parralel example

l3 = Line(Point(0, 0), Point(1, 0))
l4 = Line(Point(0, 1), Point(1, 1))

print(l3.is_parallel(l4))
print(l3.is_perpendicular(l4))
print(l3.intersection(l4))