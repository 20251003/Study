import turtle

screen = turtle.Screen()
screen.setup(width=350, height=250)

t = turtle.Turtle()


def draw_rectangle(x, y, w, h, gradient, p_size=1, p_color='black', f_color=None):
    t.penup()
    t.goto(x,y)
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

draw_rectangle(0,-100,300,200,gradient=0)

turtle.done()