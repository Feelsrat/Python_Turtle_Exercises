import turtle as t
import random

turtle = t.Turtle()
turtle.shape("arrow")
turtle.color("blue")
turtle.width(10)
turtle.speed(0)
t.colormode(255)
is_on = True


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


angles = [0, 90, 180, 270]
while is_on:
    turtle.color(random_color())
    turtle.rt(random.choice(angles))
    turtle.forward(25)

screen = t.Screen()
screen.exitonclick()
