import turtle as t

class point:                            # x, y 설정 / 펜 설정

    x = 0
    y = 0

    def __init__(self, a, b):

        self.x = a
        self.y = b
        
        t.penup()
        t.goto(a, b)
        t.pendown()

    def rot(self, a):
        
        h = t.heading() 
        h = 360-h

        t.left(h)
        t.left(a)

    def pen(self, color, size):

        t.pencolor(color)
        t.pensize(size)
        

class draw(point):

    def sq(self, w, h):                 # x, y 를 중심으로 사각형 그리기

        t.penup()                       # w는 가로, h는 세로
        t.fd(w/2)
        t.pendown()

        t.left(90)
        t.fd(h/2)
        t.left(90)
        t.fd(w)
        t.left(90)
        t.fd(h)
        t.left(90)
        t.fd(w)
        t.left(90)
        t.fd(h/2)

        t.penup()
        t.goto(self.x, self.y)
        self.rot(0)
        t.pendown()

    def tr(self, w, h):                 # x, y 를 중심으로 삼각형 그리기

        t.penup()                       # w는 밑변, h는 높이
        t.left(90)
        t.fd(h/2)

        p = t.pos()

        t.right(180)
        t.fd(h)
        t.right(90)
        t.fd(w/2)

        q = t.pos()
        
        t.pendown()

        t.left(180)
        t.fd(w)
        t.goto(p)
        t.goto(q)

        t.penup()
        t.goto(self.x, self.y)
        self.rot(0)
        t.pendown()

    def cir(self, r, a):                    # x, y 를 중심으로 원하는 각도만큼의 원 그리기

        t.penup()                           # r은 반지름, a는 원하는 각도
        t.right(90)
        t.fd(r)
        self.rot(0)
        t.pendown()

        t.circle(r, a)

        t.penup()
        t.goto(self.x, self.y)
        self.rot(0)
        t.pendown()

    def line(self, d, a):                   # x, y에서 a방향으로 d 만큼 직선

        self.rot(a)
        t.fd(d)

