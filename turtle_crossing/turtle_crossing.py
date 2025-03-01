from inspect import trace
import turtle
import turtle_class
import time
import random

screen = turtle.Screen()
screen.screensize(turtle_class.SCREEN_WIDTH, turtle_class.SCREEN_HEIGHT)
screen.colormode(255)

screen.tracer(0)
frame = turtle_class.Frame()
tur1 = turtle_class.WalkingTurtle()
# screen.tracer(1)

car_list = []
sleep_time = turtle_class.SLEEP_TIME
car_move_distance = turtle_class.CAR_MOVE_DISTANCE
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    
    # screen.tracer(0)
    if random.randint(1, 6) == 1:
        car = turtle_class.Car(); car_list.append(car)
    for car in car_list:
        car.forward(car_move_distance)  
        
        # turtle collide with car  
        if car.xcor() - 10*turtle_class.CAR_WIDTH_STRETCH <= 0 <= car.xcor() + 10*turtle_class.CAR_WIDTH_STRETCH:
            if car.ycor() - 15 <= tur1.ycor() <= car.ycor() + 15:
                tur1.color("red")
                game_is_on = False; frame.game_over()    

        if car.xcor() < -turtle_class.SCREEN_WIDTH*1.5: # remove gone cars
            car.hideturtle(); car_list.remove(car)
    # screen.tracer(1) 

    if tur1.ycor() > turtle_class.SCREEN_HEIGHT: # turtle successfully cross the road
        turtle_class.LEVEL += 1
        car_move_distance += 2
        # sleep_time *= 0.9

        frame.clear(); frame = turtle_class.Frame()
        tur1.goto(0, -screen.canvheight)
        
    
    screen.listen()
    screen.onkey(lambda: tur1.forward(20), "Up")


screen.exitonclick()
    





screen.exitonclick()
