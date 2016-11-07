import turtle
import math
wn = turtle.Screen()
alex = turtle.Turtle()

#alex.forward(20)
#alex.left(20)
#alex.color("blue")
#alex.pensize(3)

#for i in range(5):
#    alex.forward(50)
#    alex.left(50)

#clrs = ["yellow", "red", "purple", "blue"]
#for c in clrs:
#    alex.color(c)
#    alex.forward(50)
#    alex.left(90)



##Create a tuple or list with the squares based off of size

def drawgrid(size):
    square(size)
    square(size*2/3)
    square(size*1/3)
    alex.setx(size)
    alex.sety(size)
    alex.left(180)
    square(size*2/3)
    square(size*1/3)

def drawcircle(size):
    alex.forward(size/6)
    alex.circle(size/6)

def drawx(size):
    alex.left(45)
    alex.forward(size/3*math.sqrt(2))
    alex.left(135)
    alex.forward(size/3)
    alex.left(135)
    alex.forward(size/3*math.sqrt(2))
    alex.left(225)
    alex.forward(size/3)
    alex.left(180)
    
def square(size):
    for i in range(4):
        alex.forward(size)
        alex.left(90)
    
