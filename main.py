import turtle as t
import math
angle = 0
v = 0
vx = 0;
vy = 0;
dx = 0;
dy = 0;
g = 9.8
tm = 0.3
distance = 0;
height = 0;

def draw_pos(x,y):
    v = t.numinput("입력","속력:",50,10,100)
    angle = math.radians(t.numinput("입력","각도:",45,0,360))
    t.hideturtle()
    t.goto(-200, 150)
    t.clearstamps()
    t.hideturtle()
    t.showturtle()
    t.stamp()
    hl = -(t.window_height() / 2)
    ux = v * math.cos(angle)
    uy = v * math.sin(angle)
    while True:
        uy = uy + (-1*g)*tm
        dy = t.ycor() + uy - (g*tm)
        dx = t.xcor() + (ux*tm)
        if dy > hl:
            t.goto(dx,dy)
            t.stamp()
        else:
            break;

t.setup(800,800)
t.shape('circle')
t.shapesize(0.5,0.5,0)
t.speed(1)
t.penup()
s = t.Screen()
s.onscreenclick(draw_pos)
s.listen()
t.done()