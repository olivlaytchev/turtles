import turtle
import math
from collections import namedtuple


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
class TicTacToe:
        
        def __init__(self, fieldSize):
            size = fieldSize
            wn = turtle.Screen()
            self.alex = turtle.Turtle()
            #self.createSquare(size)
            self.square(size)
            self.square(size*2/3)
            self.square(size/3)
            self.alex.setx(size)
            self.alex.sety(size)
            self.alex.left(180)
            self.square(size*2/3)
            self.square(size/3)
            self.alex.left(180)
            self.alex.penup()
            self.alex.setpos(0,0)
            self.alex.pendown()

        def square(self, size):
            for i in range(4):
                self.alex.forward(size)
                self.alex.left(90)

        def drawcircle(self, size):
            #self.alex.setpos(place[0], place[1])
            self.alex.forward(size/6)
            self.alex.circle(size/6)
            self.alex.penup()
            self.alex.setpos(0,0)
            self.alex.pendown()

        def drawx(self, size):
            #self.alex.setpos(place[0], place[1])
            self.alex.left(45)
            self.alex.forward(size/3*math.sqrt(2))
            self.alex.left(135)
            self.alex.forward(size/3)
            self.alex.left(135)
            self.alex.forward(size/3*math.sqrt(2))
            self.alex.left(225)
            self.alex.forward(size/3)
            self.alex.left(180)
            self.alex.penup()
            self.alex.setpos(0,0)
            self.alex.pendown()

        def createSquare(self, size):
            Square = namedtuple("Square",(x,y))
            self.grid = {Square(size*2/3,0):7, Square(size*2/3,size/3):8, Square(size*2/3,size*2/3):9, Square(size/3,0):4, Square(size/3,size/3):5,Square(1,size*2/3):6, Square(0,0):1, Square(0,size/3):2, Square(0,size*2/3):3}


    

    
    
