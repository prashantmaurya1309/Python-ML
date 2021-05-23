import turtle
import random

colors = ['red','green','yellow']

for _ in range(30):
    turtle.pencolor(random.choice(colors))
    turtle.forward(50)
    turtle.right(144)

turtle.done()