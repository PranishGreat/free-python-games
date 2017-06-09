"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.

"""

from random import *
from turtle import *
from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)

def wrap(value):
    "Wrap value around -200 and 200."
    if value > 200:
        return -200
    if value < -200:
        return 200
    return value

def draw():
    "Move ant and draw screen."
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)

    goto(ant.x, ant.y)
    color(abs(ant.x), abs(ant.y), 200)
    dot(4)

    if running:
        ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
colormode(255)
running = True
draw()
done()
