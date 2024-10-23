import random
import turtle
from math import *
from turtle import *



pluma = turtle.Turtle()

header_text= " Chingas "
color("Blue")
penup()
goto(120,50)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))
header_text= " a tu cola "
color("Purple")
penup()
goto(120,30)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))
header_text= " DEMIAN "
color("red")
penup()
goto(120,90)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))


pluma.forward(100)
pluma.left(90)
pluma.forward(100)
pluma.left(90)
pluma.forward(20)
pluma.left(90)
pluma.forward(20)
pluma.left(180)
pluma.forward(20)
pluma.left(90)
pluma.forward(25)
pluma.left(90)
pluma.forward(20)
pluma.left(180)
pluma.forward(20)
pluma.left(90)
pluma.right(90)
pluma.forward(45)
pluma.left(90)
pluma.forward(20)
pluma.left(90)
pluma.forward(15)
pluma.left(90)
pluma.forward(20)
pluma.left(180)
pluma.forward(20)
pluma.left(90)
pluma.forward(50)
pluma.left(180)
pluma.forward(20)
pluma.left(90)
pluma.forward(20)
pluma.left(90)
pluma.forward(75)
pluma.right(90)
pluma.forward(3)
pluma.right(90)
pluma.forward(30)
pluma.left(90)
pluma.forward(15)
pluma.left(90)
pluma.forward(60)

turtle.done()