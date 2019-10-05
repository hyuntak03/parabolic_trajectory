import turtle as t
import math
b = t.Turtle()
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
b.hideturtle()
distance = t.numinput("입력","거리:",200,50,600)
height = t.numinput("입력","높이:",150,100,200)
b.penup()
b.setpos(distance-200,150)
b.pendown()
b.left(90)
b.forward(height-60)
b.circle(30)
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
t.goto(-200,150)
s = t.Screen()
s.onscreenclick(draw_pos)
s.listen()
t.done()