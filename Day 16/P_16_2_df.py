import turtle as t

p = t.Turtle()          # 펜 객체
    
scr = t.Screen()        # 스크린 객체

def ch_s():             # 함수 실행 시 텍스트 입력창 띄워 입력받은 값으로 모양 변경

    s = t.textinput("SHAPE", "Enter : ")
    p.shape(s)
    scr.listen()        # 입력창 실행시 이벤트를 다시 들어야함

def ch_c():             # 함수 실행 시 입력창 띄워 입력받은 값으로 색 변경

    c = t.textinput("COLOR", "Enter : ")
    p.color(c)
    scr.listen()

def fill():             # 함수 실행 시 채색 시작

    p.begin_fill()

def e_fill():           # 채색 완료
                        # 시작 함수가 실행된 이후부터 이 함수 실행까지 채색함
    p.end_fill()

def rt_l():             # 왼쪽으로 30도 회전

    p.left(30)

def rt_r():             # 오른쪽으로 30도 회전

    p.right(30)

def up():               # 북쪽으로 방향틀기

    a = p.heading()

    p.right(a)
    p.left(90)

def down():             # 남쪽으로 방향틀기

    a = p.heading()

    p.right(a)
    p.right(90)

def left():             # 서쪽으로 방향틀기

    a = p.heading()

    p.right(a)
    p.left(180)

def right():            # 동쪽으로 방향틀기

    a = p.heading()

    p.right(a)

def p_up():             # down 상태라면 들고 up 상태라면 내린다.

    if p.isdown(): p.penup()
    else: p.pendown()

def reset():            # 시작위치로 돌아가기

    p.goto(0, 0)

def end():              # 프로그램 종료

    scr.bye()

