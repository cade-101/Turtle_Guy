from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(0, 260)
        self.write(f"Level: {self.level}", align='center', font=('Courier', 32, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER. Level: {self.level}", align='center', font=('Courier', 32, 'normal'))

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=('Courier', 32, 'normal'))