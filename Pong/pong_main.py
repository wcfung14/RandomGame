from pickle import FRAME
import turtle
import pong_class
import pong_ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = turtle.Screen()
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong game")

left_player_score = 0
right_player_score = 0

screen.tracer(False)
frame = pong_class.Frame()

# left_paddle = pong_class.Paddle()
# left_paddle.make_left_paddle()
# right_paddle = pong_class.Paddle()
# right_paddle.make_right_paddle()

left_paddle = pong_class.Paddle(-frame.FRAME_WIDTH+30, 0)
right_paddle = pong_class.Paddle(frame.FRAME_WIDTH-30, 0)
screen.tracer(True)

ball = pong_ball.Ball()

ball.start()
sleep_time = 0.01

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up") 
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

while True:    
    time.sleep(sleep_time)
    ball.move()
    

    if abs(ball.xcor())+20 > right_paddle.xcor() and (ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50):
        ball.x_bounce()
        sleep_time *= 0.95
        print(sleep_time)
        
    if ball.ycor() > frame.FRAME_HEIGHT-30 or ball.ycor() < -frame.FRAME_HEIGHT+30:
        ball.y_bounce()
    
    if ball.xcor() > frame.FRAME_WIDTH or ball.xcor() < -frame.FRAME_WIDTH:
        if ball.xcor() > frame.FRAME_WIDTH:
            left_player_score += 1
        elif ball.xcor() < -frame.FRAME_WIDTH:
            right_player_score += 1
        screen.tracer(False)
        frame.update(left_player_score, right_player_score); ball.start()
        screen.tracer(True)
        time.sleep(2)
        sleep_time = 0.01




screen.exitonclick()
