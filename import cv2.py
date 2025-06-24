import turtle
import random

t= turtle.Turtle()
s = turtle.getscreen()
s.bgcolor("black")
t.pencolor("white")
t.speed(100)
col=('red','blue','green','yellow','purple','orange','pink')


for n in range(5):
    for x in range(8):
        t.speed(x + 10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()            
            
   