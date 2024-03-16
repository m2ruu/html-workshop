from turtle import *
from random import *
speed(100)
colormode(255)

for i in range(100):
    color(randint(50, 255), randint(50, 255), randint(50, 255))
    penup()
    goto(randint(-450,450), randint(-450,450))
    pendown()
    if randint(0,2)==1:
        begin_fill()
        circle(randint(10,100))
        end_fill()
    elif randint(0,2)==0:
        begin_fill()
        pikkus=randint(20,100)
        forward(pikkus)
        right(120)
        forward(pikkus)
        right(120)
        forward(pikkus)
        end_fill()
    else:
        begin_fill()
        pikkus=randint(20,100)
        for i in range(4):
            forward(pikkus)
            right(90)
        end_fill()

exitonclick()