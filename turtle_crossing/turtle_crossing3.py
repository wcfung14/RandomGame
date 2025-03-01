import turtle as tr
import random
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Player(tr.Turtle):
    def __init__(self, screen_height, shape = "turtle"):
        super().__init__(shape)
        self.penup()
        self.goto(0, -screen_height/2+20)
        self.setheading(90)
    
    def move(self, screen):
        screen.onkeypress(lambda: self.forward(20), "Up")
    
class Car(tr.Turtle):
    def __init__(self, screen_width, screen_height, shape = "square"):
        super().__init__(shape)
        self.shapesize(stretch_wid = 1, stretch_len=3)
        self.penup()
        self.setheading(180)
        self.goto(SCREEN_WIDTH/2, random.randint(-int(screen_height/2)+40, int(screen_height/2)))

    def move(self):
        self.forward(random.randint(10, 30))

    def detect_collision(self, player):
        return self.distance(player.pos()) < 19
            
class CarManager():
    def __init__(self):
        self.car_list = list()

    def make_car(self, car):
        self.car_list.append(car)

screen = tr.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

player = Player(SCREEN_HEIGHT)

car_manager = CarManager()

game_is_on = True
while game_is_on:
    player.move(screen)
    if random.choice([1, 0, 0]):
        car_manager.make_car(Car(SCREEN_WIDTH, SCREEN_HEIGHT))

    for car in car_manager.car_list:
        car.move()
        if car.detect_collision(player):
            print("gg!")
        if car.xcor() < -SCREEN_WIDTH/2-100:
            car_manager.car_list.remove(car)

    time.sleep(0.1)
    screen.update()