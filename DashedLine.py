from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue")

for _ in range(15):
    turtle.pd()
    turtle.forward(10)
    turtle.pu()
    turtle.forward(10)

screen = Screen()
screen.exitonclick()