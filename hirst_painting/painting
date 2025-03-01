import turtle
import heroes
import random 
import colorgram

# print(heroes.genarr(9))

tr = turtle.Turtle()
tr.shape("turtle")
tr.color("DarkRed")
tr.speed("fastest")

screen = turtle.Screen()
screen.colormode(255)


# def drawdot(space,x):
#   for i in range(x):
#     for j in range(x):
#         tr.dot()
#         tr.forward(space)
#     tr.backward(space*x)
      
#     tr.right(90)
#     tr.forward(space)
#     tr.left(90)

# tr.penup()
# drawdot(10,8)

## draw square 
# i = 0
# while True:
#     tr.hideturtle()
#     j = [90, 60, 70, 110]
#     tr.forward(j[i % 4])
#     tr.left(90)
#     i += 1
#     if abs(tr.pos()) < 1:
#         break

## draw polygons
# side = 4
# while True:
#     for _ in range(side):
#         tr.forward(100)
#         tr.left(360 / side)
#     tr.pencolor((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
#     side += 1
#     if side > 10:
#         break

## random walk
# tr.width(3)
# for i in range(1000):
#     tr.write(i)
#     tr.pencolor((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
#     tr.forward(10)
#     tr.setheading(random.choice([0, 90, 180, 270]))

## draw spirograph
# for i in range(0,361, 5):
#     tr.pencolor((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
#     tr.setheading(i)
#     tr.circle(100)

## hirst-painting
# extract color by colorgram
colors = colorgram.extract("hirst_painting\Cat03.jpg", 30)
colors_rgb = []
for i in colors:
    colors_rgb.append((i.rgb.r, i.rgb.g, i.rgb.b))

print(colors_rgb)

tr.penup()
def draw_dot(x, y, step):
    for j in range(y):
        for i in range(x):
            # tr.pencolor((random.randint(s1,255), random.randint(1,255), random.randint(1,255)))
            tr.dot(11, random.choice(colors_rgb))
            tr.forward(step)
       
        tr.backward(step*x)
        tr.right(90)
        tr.forward(step)
        tr.left(90)
            
draw_dot(10,10,20)
tr.hideturtle()

screen.exitonclick()
