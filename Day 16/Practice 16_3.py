##import msvcrt
##
##while 1:
##    print(ord(msvcrt.getch()))
##                          # 키보드 입력시 그때그때 바로 단일문자를 읽어옴
### IDEL 스크립트에서 작성시 제대로 실행되지 않는다.

import turtle as t

class pt:                   # pt는 하나의 좌표
    
    x = 0
    y = 0

    def __init__(self, x, y):
                            # 입력된 x, y에 따라 x, y가 지정된다.
        self.x = x
        self.y = y

# function

def line(p1, p2):           # 서로다른 객체 p1, p2 의 사이를 이어주는 선을 그리는 함수

    t.penup()
    t.goto(p1.x, p1.y)
    t.pendown()
    t.goto(p2.x, p2.y)


# main

p1 = pt(0, 0)               # 처음 p1은 0, 0

while 1:

    k = input()             # 문자열을 입력을 받고

    if (k.lower() == "x") |(k.lower() == "q"): break
                            # x 나 q 가 들어온다면 break
    if k.lower() == "w": p2 = pt(p1.x, p1.y + 50)
                            # w 가 들어온다면 p2는 p1에서 y축으로만 +50 전진
    elif k.lower() == "a": p2 = pt(p1.x - 50, p1.y)
                            # a 가 들어온다면 p2는 p1에서 x축으로만 -50
    elif k.lower() == "s": p2 = pt(p1.x, p1.y - 50)
                            # s 가 들어온다면 p2는 p1에서 y축으로만 -50
    elif k.lower() == "d": p2 = pt(p1.x + 50, p1.y)
                            # d 가 들어온다면 p2는 p1에서 x축으로면 +50
    line(p1, p2)            # 둘 사이를 이어주면
                            # 입력에 따라 해당 방향으로 전진하며 직선을 그린다.
    p1 = pt(p2.x, p2.y)     # line이 실행되면 현재 좌표가 바뀌기에
                            # p1 = p2의 좌표
