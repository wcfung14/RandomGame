import turtle
import random

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
    
    def start(self):
        self.goto(0, 0)
        self.x_move = 5
        self.y_move = random.randint(1, 10)
        self.x_move *= -1 if random.randint(1,2) == 1 else 1
        self.y_move *= -1 if random.randint(1,2) == 1 else 1
        
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        
    def x_bounce(self):
        self.x_move = (abs(self.x_move) + 1) * (self.x_move/abs(self.x_move))
        print(abs(self.x_move))
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1