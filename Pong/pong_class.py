import turtle
import random
import time

SCREEN_WIDTH = 200
PADDLE_LENGTH = 3

# PADDLE_PART_POS = [0, 20, -20, 40, -40]

class Frame(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.FRAME_WIDTH = 380
        self.FRAME_HEIGHT = 280 
        
        self.new_frame(0, 0)

    def new_frame(self, left_player_score, right_player_score): 
        self.color("white"); self.hideturtle()
        self.penup(); self.goto(self.FRAME_WIDTH, self.FRAME_HEIGHT)
        self.pendown()
        self.goto(self.FRAME_WIDTH, -self.FRAME_HEIGHT); self.goto(-self.FRAME_WIDTH, -self.FRAME_HEIGHT); self.goto(-self.FRAME_WIDTH, self.FRAME_HEIGHT); self.goto(self.FRAME_WIDTH, self.FRAME_HEIGHT)
        self.penup()
        self.goto(0, self.FRAME_HEIGHT-50); self.write(f"{left_player_score}  {right_player_score}", align="center", font=("Arial", 30, "normal"))
        self.goto(0, self.FRAME_HEIGHT); self.setheading(270)
        while True:
            if self.ycor() != -self.FRAME_HEIGHT:
                self.dot(); self.forward(20); self.dot()
            else:
                break
    
    def update(self, left_player_score, right_player_score):
        self.clear()
        self.new_frame(left_player_score, right_player_score)


class Paddle(turtle.Turtle):
    # def __init__(self):
    # #     super().__init__()
    #     self.paddle_list = []
    #     for i in range (0, PADDLE_LENGTH):
    #         self.paddle = turtle.Turtle()
    #         self.paddle.shape("square")
    #         self.paddle.color("white")
    #         self.paddle.penup()
    #         self.paddle_list.append(self.paddle)
    #     print(self.paddle_list)

    # def make_left_paddle(self):
    #     for i in range(0, PADDLE_LENGTH):
    #         self.paddle_list[i].goto(-SCREEN_WIDTH, PADDLE_PART_POS[i])
    #         print(self.paddle_list[i].pos())

    # def make_right_paddle(self):
    #     for i in range(0, PADDLE_LENGTH):
    #         self.paddle_list[i].goto(SCREEN_WIDTH, PADDLE_PART_POS[i])
    #         print(self.paddle_list[i].pos())
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        
    
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
        

