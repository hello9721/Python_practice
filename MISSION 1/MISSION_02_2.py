# Q2 수학 함수를 이용하여 그리기 -> sin, cos, tan / 원 / 원 안의 sin

import math as m
import turtle as t              # 그래프를 그려줄 패키지 import


# sin, cos, tan

x_min = -360                    # x 범위
x_max = 360

y_min = -2                      # y 범위
y_max = 2

t.setworldcoordinates(x_min, y_min, x_max, y_max)
                                # 그래프 범위 설정
t.speed(0)
t.pensize(2)

t.up()                          # 그리지 않고 커서 이동
t.goto(x_min, 0)                # x축 시작지점부터
t.down()                        # 그리면서 이동
t.goto(x_max, 0)                # x축 끝지점까지

t.up()                          # y축도 그리기
t.goto(0, y_min)
t.down()
t.goto(0, y_max)


t.color("blue")                 # sin 그래프는 파란색으로

x = -360                        # 첫 시작지점 x
y = m.sin(m.pi * (x / 180) )    # 첫 시작지점 y

t.up()                          # 커서를 x, y로 이동 시키고
t.goto(x, y)
t.down()                        # 그리면서

for i in range(-359, 360):      # 범위 만큼 반복하여

    x = i
    y = m.sin(m.pi * x / 180 )

    t.goto(x, y)                # 그래프 그리면서 좌표 이동


t.color("green")                # cos 그래프는 초록색으로

x = -360                        # x, y 첫 지점 부터
y = m.cos(m.pi * x / 180 )

t.up()
t.goto(x, y)
t.down()                        # 그리면서

for i in range(-359, 360):
    
    x = i
    y = m.cos(m.pi * x / 180 )

    t.goto(x, y)                # x, y 이동


t.color("red")                  # tan 그래프는 빨강으로

x = -360
y = m.tan(m.pi * x / 180 )

t.up()
t.goto(x, y)
t.down()

for i in range(-359, 360):      # 똑같이 그리기
    
    x = i
    y = m.tan(m.pi * x / 180 )

    t.goto(x, y)


# 원 그리기

x_min = -500                    # x 범위
x_max = 500

y_min = -500                    # y 범위
y_max = 500

t.setworldcoordinates(x_min, y_min, x_max, y_max)
                                # 그래프 범위 설정

p = t.Pen()                     # Pen 기능 사용

t.up()                          # 0, 0 으로 이동
t.goto(0,0)

p.dot(720, "black")           # 0, 0을 중심으로 배경이 까만 원 그리기


# 원 안에 sin 그래프

x_min = -500                    # x 범위
x_max = 500

y_min = -500                    # y 범위
y_max = 500

t.setworldcoordinates(x_min, y_min, x_max, y_max)
                                # 그래프 범위 설정
p = t.Pen()

t.up()
t.goto(0,0)

p.dot(720, "black")             # 배경이 까맣고 지름이 720이 원 그리기


t.color("white")                # sin 그래프는 하얀색으로

x = -385                        # 첫 시작지점 x, y
y = m.sin(m.pi * (x / 385)) * 200
                                # 원 안에서 한 주기만, y 가 넓게 그리기 위해 수치 조정
t.pensize(10)                   

t.up()                          # 커서를 x, y로 이동 시키고
t.goto(x, y)
t.down()                        # 그리면서

for i in range(-384, 386):      # 범위 만큼 반복하여

    x = i
    y = m.sin(m.pi * (x / 385)) * 200

    t.goto(x, y)                # 그래프 그리면서 좌표 이동


