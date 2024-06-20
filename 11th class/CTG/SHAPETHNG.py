import turtle

t = turtle.Turtle()

deg = 30
t.speed(0)

def square ():
    for i in range(4):
        t.forward(100)
        t.right(90)

t.right(deg/2)

for i in range(3):
    square()
    t.right(deg+90)

turtle.done()