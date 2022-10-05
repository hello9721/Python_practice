import turtle as t
                                # 터틀 그래픽 임포트
t.shape('turtle')               # 커서 모양 거북이

## t.circle(100)                # 현재 위치에서 반지름 100의 원을 그려라
##
## t.setpos(0, 100)             # 좌표를 0, 100 으로 이동
## t.setpos(100, 100)


# 오징어게임판 그리기
# 400 100 300 세로
# 500 가로
# 오른쪽 250 왼쪽 -250
# 원 100

t.setworldcoordinates(-600, -200, 600, 1000)
                                # 그릴 범위 설정

# 위쪽 원

t.penup()                       # 이동하는 동안 그려지지 않도록 펜을 들고
t.goto(0, 675)                  # 해당 좌표로 이동
t.pendown()                     # 그려지도록 펜 내리고

t.circle(125)                   # 반지름 125인 원 그리기

# 삼각형 그리기

t.penup()
t.goto(0, 800)
t.pendown()

t.goto(-250, 500)               # 해당위치로 이동하며 직선을 그리기
t.goto(-50, 500)

# 가운데 구간

t.goto(-50, 400)

# 아래 직사각형

t.goto(-250, 400)
t.goto(-250, 0)
t.goto(250, 0)
t.goto(250, 400)
t.goto(50, 400)

# 가운데 구간

t.goto(50, 500)

# 삼각형 마무리

t.goto(250, 500)
t.goto(0, 800)

# 아래쪽 원

t.penup()
t.goto(0, -100)
t.pendown()

t.circle(100)

# 양옆의 작은 원들

t.penup()
t.goto(-250, 400)
t.pendown()

t.circle(50)

t.penup()
t.goto(250, 400)
t.pendown()

t.circle(50)
