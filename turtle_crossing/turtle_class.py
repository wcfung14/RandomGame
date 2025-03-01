import turtle
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LEVEL = 1
SLEEP_TIME = 0.05
CAR_WIDTH_STRETCH = 2
CAR_MOVE_DISTANCE = 10

class Frame(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle(); self.penup()
        self.goto(-SCREEN_WIDTH, SCREEN_HEIGHT)
        self.write(f"Level: {LEVEL}", font=("Arial", 15, "normal"))
        self.goto(SCREEN_WIDTH, SCREEN_HEIGHT); self.pendown()
        self.goto(-SCREEN_WIDTH, SCREEN_HEIGHT)

    def game_over(self):
        self.penup(); self.goto(0, 0)
        self.write("Game Over :(", align="center", font=("Arial", 20, "bold"))

class WalkingTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -SCREEN_HEIGHT)

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, CAR_WIDTH_STRETCH)
        self.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.penup()
        self.goto(random.randint(SCREEN_WIDTH, SCREEN_WIDTH+200), random.randint(-SCREEN_HEIGHT+30, SCREEN_HEIGHT-30))
        self.setheading(180)
