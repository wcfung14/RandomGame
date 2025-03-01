import turtle
import time
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

class Car(turtle.Turtle):
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.goto(SCREEN_WIDTH*0.9/2, random.randint(-SCREEN_HEIGHT*0.8/2, SCREEN_HEIGHT*0.9/2))
        self.setheading(180)
        self.pace = random.random()

    def move(self):
        self.forward(20*self.pace)

class Player(turtle.Turtle):
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.goto(0, -SCREEN_HEIGHT*0.9/2)
        self.setheading(90)
    
    def move_up(self):
        self.forward(20)

car_list = []
for _ in range(10):
    car = Car(shape="square", undobuffersize=1, visible=True)
    car_list.append(car)

player = Player(shape="turtle", undobuffersize=1, visible=True)
screen.onkey(lambda: player.forward(20), "Up")
screen.listen()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for car in car_list:
        car.move()
    screen.update()
