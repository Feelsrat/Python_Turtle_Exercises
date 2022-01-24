from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue")

for _ in range(4):
    turtle.forward(100)
    turtle.rt(90)

screen = Screen()
screen.exitonclick()