from turtle import Turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

class Car(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.color(random.choice(colors))
        self.shape('square')
        self.shapesize(1, 2)
        self.goto(xcor, ycor)
        self.x_move = 20
        self.y_move = 0


    def move_car(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

