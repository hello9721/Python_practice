import turtle as t

def set_size(l):

    l = l/2
    
    t.setworldcoordinates(-200 -l, -200 -l , 200 +l, 200 +l)

def square(width, height):

    t.penup()
    t.goto(-1*width/2, 0)
    t.pendown()
    
    t.goto(-1*width/2, height/2)
    t.goto(width/2, height/2)
    t.goto(width/2, -1*height/2)
    t.goto(-1*width/2, -1*height/2)
    t.goto(-1*width/2, 0)

def move(x, y):

    t.penup()
    t.goto(x, y)
    t.pendown()

def circle(s, r, a):

    t.color(s)
    t.begin_fill()
    t.circle(r, a)
    t.end_fill()

def fw(d):

    t.penup()
    t.forward(d)
    t.pendown()

def rt(dg):
    
    h = t.heading()
    h = 360-h

    t.left(h)
    t.left(dg)
    print(t.heading())

    
    
