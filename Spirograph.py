
'''Making a spirograph'''
from turtle import Turtle, Screen
import random
circle_turtle=Turtle()
screen=Screen()
screen.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b) #Choose a random color from rgb
    return random_color

def draw_spirograph(size_of_gap):
    for spin in range(int(360/size_of_gap)):
        circle_turtle.color(random_color())
        circle_turtle.speed("fastest")
        circle_turtle.circle(100)
        circle_turtle.setheading(circle_turtle.heading()+size_of_gap) #Setheading

draw_spirograph(4)

screen.exitonclick