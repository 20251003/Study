import turtle
import math

UNIT = 300

screen = turtle.Screen()
screen.setup(width=UNIT*3.5, height=UNIT*2.5)


t = turtle.Turtle()
t.hideturtle()


def draw_rectangle(x, y, w, h, gradient, p_size=1, p_color='black', f_color=None):
    t.penup()
    t.goto(x,y)
    t.setheading(gradient)
    t.pendown()

    t.pensize(p_size)  
    t.pencolor(p_color)  
    if f_color:
        t.fillcolor(f_color)  
        t.begin_fill()  

    t.forward(w/2)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w/2)

    if f_color:
        t.end_fill()

def draw_circle(x, y, radius, gradient, extent=180,  p_size=1, p_color='black', f_color=None):
    t.penup()
    t.goto(x,y)
    t.setheading(gradient-90)
    t.forward(50)
    t.setheading(gradient)
    t.pendown()

    t.pensize(p_size)  
    t.pencolor(p_color)  
    if f_color:
        t.fillcolor(f_color)  
        t.begin_fill()

    t.circle(radius,extent)
    
    if f_color:
        t.end_fill()

def draw_taeguek(unit=300):
    theta = math.atan(3/2)
    gradient = math.degrees(theta)
    draw_circle(0,0,unit/6,gradient,p_color='red',f_color='red')
    draw_circle(0,0,unit/6,gradient+180,p_color='blue',f_color='blue')
    draw_circle(0,0,unit/12,gradient,extent=180,p_color='blue',f_color='blue')
    draw_circle(0,0,unit/12,gradient+180,extent=180,p_color='red',f_color='red')


def draw_gun(unit=300):
    theta = math.atan(2/3)
    gradient = math.degrees(theta)
    t.penup()
    t.goto(0,0)
    t.setheading(180-gradient)
    t.forward((unit/2)+((3*unit)/4))
    x,y = t.position()
    
    draw_rectangle(x,y,unit/2,unit/12,45,f_color='black')

#def draw_gon():

#def draw_gam():

#def draw_yee():

draw_rectangle(0,-UNIT,UNIT*3,UNIT*2,gradient=0)
draw_taeguek()
draw_gun()
turtle.done()