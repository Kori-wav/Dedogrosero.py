import turtle
import time

delay = 0.1

wn = turtle.Screen()

wn.title("Juego Snake")

wn.setup(width=600, height= 600)

wn.bgcolor("Light green")


head = turtle.Turtle()

head.speed(0)

head.penup()

head.shape("square")

head.color("green")

head.goto(0, 0)
head.direction = "stop"


# config comida
food = turtle.Turtle()
food.speed(0)
food.shape ("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.direction = "stop"


def mov():
    if head.direction == "up":
        y = head.ycor()
    
        
        head.sety(y + 10)
    if head.direction == "down":
        y = head.ycor()
    
        
        head.sety(y - 10)
        
    if head.direction == "left" :
        x = head.xcor()
        head.setx(x - 10)
     
    if head.direction == "right" :
        x = head.xcor()
        head.setx(x + 10)
        

def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirLeft():
    head.direction = "left"
def dirRight():
    head.direction = "right"


wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirLeft, "Left")
wn.onkeypress(dirRight, "Right")
    
    

    
            
while True:
    wn.update()
    mov()
    time.sleep(delay)
    
    
turtle.done()