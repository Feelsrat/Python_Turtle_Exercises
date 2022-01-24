from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue")

colors = ["dark blue", "magenta", "yellow"]

def draw_shape(num_of_sides):
    for _ in range(num_of_sides):
        angle = 360 / num_of_sides
        turtle.forward(100)
        turtle.rt(angle)

for shape_side_n in range(3,11):
    turtle.color(random.choice(colors))
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()
