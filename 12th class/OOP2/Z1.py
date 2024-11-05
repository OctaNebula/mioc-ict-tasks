from math import gcd

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.shorten()
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __repr__(self):
        return str(self.num) + "/" + str(self.den)
    
    def shorten(self):
        a = gcd(self.num, self.den)
        self.num //= a
        self.den //= a
        return self

    def add(self, f):
        return Fraction(self.num * self.den + f.num * f.den, self.den * f.den)

    def power(self, n):
        return Fraction(self.num ** n, self.den ** n)
    
    def greaterthan(self, f):
        return self.num / self.den > f.num / f.den
    
    # Magic methods use to simplify usage (we were told not to use them to make .add() as a practice)

    def __add__(self, f):
        return self.add(f)

    def __pow__(self, n):
        return self.power(n)
