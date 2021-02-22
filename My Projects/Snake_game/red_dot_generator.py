from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)


def change():
    food.x = randrange(-12, 12) * 8
    food.y = randrange(-12, 12) * 8


def red_dot_generator():
    clear()
    square(food.x, food.y, 9, 'red')
    update()
    ontimer(red_dot_generator, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(), 'plus')
onkey(lambda: change(), 'space')
red_dot_generator()
done()
