import turtle as tr
import time

BOARD_WIDTH = 16*50
BOARD_HEIGHT = 9*50

screen = tr.Screen()
screen.setup(width=BOARD_WIDTH*1.2, height=BOARD_HEIGHT*1.2)
screen.tracer(0)

class Paddle(tr.Turtle):
    def __init__(self, x_cor, shape = "square"):
        super().__init__(shape)
        self.STRETCH_LEN = 5 
        self.turtlesize(stretch_wid=1, stretch_len=self.STRETCH_LEN)
        self.setheading(90)
        self.penup()
        self.goto(x_cor, 0)

    def move(self, screen, up_key, down_key):
        screen.onkeypress(lambda: self.forward(20) if self.ycor() < screen.screensize()[1]/2 else None, up_key)
        screen.onkeypress(lambda: self.backward(20) if self.ycor() > -screen.screensize()[1]/2 else None, down_key)

    def hit_ball(self, ball, x_limit):
        self.PADDLE_LEN = 20 * self.STRETCH_LEN
        if abs(ball.xcor()) >= x_limit/2*0.85 and self.distance(ball)<50:
            print(f"{self.ycor() - self.PADDLE_LEN/2} ------------ {self.ycor() + self.PADDLE_LEN/2}")
            if self.ycor() - self.PADDLE_LEN/2 <= ball.ycor() <= self.ycor() + self.PADDLE_LEN/2:
                ball.bounce_x()


class Ball(tr.Turtle):
    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.penup()
        self.vertical_dir = 1
        self.horizontal_dir = 1
    
    def move(self):
        self.setx(self.xcor() + 5 * self.horizontal_dir)
        self.sety(self.ycor() + 5 * self.vertical_dir)
    
    def bounce_y(self, y_limit):
        if abs(self.ycor()) > y_limit/2-10:
            self.vertical_dir *= -1

    def bounce_x(self):
        self.horizontal_dir *= -1


class Board(tr.Turtle):
    def __init__(self, board_width, board_height):
        super().__init__()
        self.speed(0)
        self.penup()    
        self.goto(board_width/2, board_height/2)
        self.pendown()
        for _ in range(2):        
            self.right(90)
            self.forward(board_height)
            self.right(90)
            self.forward(board_width)
        self.hideturtle()

board = Board(BOARD_WIDTH, BOARD_HEIGHT)
player1_paddle = Paddle(x_cor=BOARD_WIDTH/2*0.9)
player2_paddle = Paddle(x_cor=-BOARD_WIDTH/2*0.9)
ball = Ball()

while True:
    screen.listen()
    screen.update()
    player1_paddle.move(screen=screen, up_key="Up", down_key="Down")
    player2_paddle.move(screen=screen, up_key="w", down_key="s")
    ball.move()
    ball.bounce_y(y_limit = BOARD_HEIGHT)
    
    player1_paddle.hit_ball(ball, x_limit=BOARD_WIDTH)
    player2_paddle.hit_ball(ball, x_limit=BOARD_WIDTH)


    time.sleep(0.02)



screen.mainloop()