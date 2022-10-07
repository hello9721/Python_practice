import turtle as t

#### 설정

def set_size(l):                    # 0,0 을 중심으로 여유여백 200씩 가
                                    # l * l 크기의 정사각형으로 설정

    l = l/2
    
    t.setworldcoordinates(-200 -l, -200 -l , 200 +l, 200 +l)
    

#### 이동

def move(x, y):                     # x, y 좌표로 그리지 않고 이동

    t.penup()
    t.goto(x, y)
    t.pendown()
    

def fw(d):                          # 앞으로 d 만큼 그리지 않고 이동

    t.penup()
    t.forward(d)
    t.pendown()
    

#### 그리기

def line(l):                        # 현재 바라보고 있는 방향 기준
                                    # 앞으로 l 만큼 전진하며 직선 그리기
    t.pendown()
    t.forward(l)
    t.penup()
    

def circle(s, r, a):                # 원을 그릴때는 90도를 더 돌아 그려진다.

    t.color(s)                      # 받은 색 이름의 색으로
    t.begin_fill()                  # 채운
    t.circle(r, a)                  # r 만큼의 반지름으로 a 도 만큼만
    t.end_fill()                    # 그려서 채우


def square(a, c, width, height):    # 현재 바라보고 있는 방향에 사각형 그리기

    t.color(c)                      # c 라는 색으로 색칠 시작
    t.begin_fill()
    
    rt(90+a)                        # 현재 방향(a)에서 90도로 돌아서
    line(height/2)                  # 높이의 반만큼만 직선 그리기

    rt(0+a)                         # -90도로 돌아서
    line(width)                     # 너비 만큼 직선 그리기

    rt(360-90+a)                    # -90도로 돌아서
    line(height)                    # 높이 만큼 직선 그리기

    rt(180+a)                       # -90도로 돌아서
    line(width)                     # 너비 만큼 직선 그리기

    rt(90+a)                        # -90도로 돌아서
    line(height/2)                  # 마무리
    
    t.end_fill()                    # 색칠 끝
    

def edge(a, d, mode):               # 괘 그리기

    if mode == 0:

        rt( a )                     # a 도 방향으로
        fw( d )                     # d 만큼 전진
                                    # a 도 방향에 검은색 사각형
        square( a, "black", 200, 1200 )

    elif mode == 1:

        rt( a )                     # a 도 방향으로 d 전진
        fw( d )
                                    # 검은색 사각형
        square( a, "black", 200, 1200 )       

        rt( a )                     # 다시 a 도로 돌아
                                    # 검은 사각형 가운데 부분을 하얗게 지워주기
        square( a, "white", 200, 100 )



#### 회전

def rt(dg):                         # 바라보는 각도가 0이면 오른쪽을 바라본다.
                                    # 항상 0 을 기준으로 바라보는 방향이
    h = t.heading()                 # 반시계방향으로 dg 가 되게 하는 함수
    h = 360-h

    t.left(h)                       # 각도가 0이 되고
    t.left(dg)                      # 다시 dg만큼 왼쪽으로 돌기

    
    
