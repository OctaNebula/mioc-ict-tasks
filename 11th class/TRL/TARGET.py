import turtle
t = turtle.Turtle()
t.speed(0)

#draws a target with 10 cocentric circles while filling the alternate circles with red and white color
#also should begin drawing with the largest circle and end with the smallest circle
turtle.hideturtle()

def target():
    for i in range(10,0,-1):
        t.penup()
        t.goto(0,-10*i)
        t.pendown()
        if i%2==0:
            t.fillcolor("red")
        else:
            t.fillcolor("white")
        t.begin_fill()
        t.circle(10*i)
        t.end_fill()


target()