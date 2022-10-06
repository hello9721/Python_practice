import turtle as t

def move(x, y):

    t.penup()
    t.goto(x,y)
    t.pendown()

def angle(x):

    move(0, 800)
    
    t.goto(250 * x, 500)
    t.goto(50 * x, 500)

def draw(x, y, g_x, g_y):

    move(x, y)
    t.goto(g_x, g_y)
