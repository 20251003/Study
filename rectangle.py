import turtle
import math

t = turtle.Turtle()

def draw_rectangle(x,y,w,h,gradient,p_size=1,p_color='black',f_color=None):
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

def draw_gun(unit=300):
    radiaus = math.atan(2/3)
    degrees = math.degrees(radiaus)
    t.penup()
    t.goto(0,0)
    t.setheading(180-degrees)
    t.forward((3*unit)/4)
    
    for _ in range(3):
        x, y = t.position()
        draw_rectangle(x, y, unit / 2, unit / 12, 90 - degrees, f_color='black')
        t.penup()
        t.setheading(180 - degrees)
        t.forward(unit / 8)
        t.pendown()

def draw_gon(unit=300):
    radiaus = math.atan(2/3)
    degrees = math.degrees(radiaus)
    t.penup()
    t.goto(0,0)
    t.setheading(degrees)
    t.forward((3*unit)/4)
    
    for _ in range(3):
        x, y = t.position()
        draw_rectangle(x, y, unit / 2, unit / 12, -degrees, f_color='black')
        t.penup()
        t.setheading(degrees)
        t.forward(unit / 8)
        t.pendown()


draw_gun()
draw_gon()
#draw_gam()
#draw_yee()
turtle.done()

