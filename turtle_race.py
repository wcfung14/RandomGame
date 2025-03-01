import turtle as tr
import random

tim = tr.Turtle()
screen = tr.Screen()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win?")

tim.penup()
tim.goto(SCREEN_WIDTH/2*0.9, SCREEN_HEIGHT/2*0.9)
tim.pendown()
tim.goto(SCREEN_WIDTH/2*0.9, -SCREEN_HEIGHT/2*0.9)

t_dict = dict()
t_list = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(len(t_list)):
    color = t_list[i]
    t_dict[color] = tr.Turtle(shape="turtle")
    t_dict[color].color(color)
    t_dict[color].penup()
    t_dict[color].goto(-SCREEN_WIDTH/2*0.9, (SCREEN_HEIGHT*0.8)/len(t_list)*i - (SCREEN_HEIGHT*0.8)/2)

notWin = True
while notWin:
    print(SCREEN_WIDTH/2*0.9)
    for k, v in t_dict.items():
        v.forward(random.randint(0, 10))
        print(k)
        print(v.pos())
        print(v.pos()[0])
        if v.pos()[0] > SCREEN_WIDTH/2*0.9:
            winner = k
            print(winner)
            notWin = False

print(user_bet.lower() == winner.lower())


print(t_dict)





screen.exitonclick()