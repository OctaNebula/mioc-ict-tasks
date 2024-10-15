import math

class Complex():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def output(self, real, imag):
        print(f"z = {real} + {imag}i")
    
    def modulus(self, real, imag):
        mod = int(math.sqrt(real**2 + imag**2))
        print(f"Mod = {mod}")
        
# example

z = Complex(3, 4)

z.output(z.real, z.imag)
z.modulus(z.real, z.imag)
