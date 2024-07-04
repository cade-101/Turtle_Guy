from turtle import Turtle

class Guy(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('blue')
        self.setheading(90)
        self.goto(0, -280)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.reset()
        self.penup()
        self.shape('turtle')
        self.color('blue')
        self.setheading(90)
        self.goto(0, -280)