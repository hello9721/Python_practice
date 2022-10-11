# 터틀 패키지
# 함수 정의 및 사용
# 키보드 이용 그리기

from P_16_2_df import *


speed = 1                       # 초반 스피드

def sp_up():                    # 함수 실행 시 스피드 +1
    
    global speed
    speed +=1

def sp_down():                  # 함수 실행 시 스피드 -1

    global speed
    speed -=1


scr.listen()                    # 이벤트 듣기

scr.onkey(rt_l, "Left")         # 설정키 누르면 해당 함수 실행
scr.onkey(rt_r, "Right")
scr.onkey(sp_up, "Up")
scr.onkey(sp_down, "Down")

scr.onkey(up, "w")
scr.onkey(left, "a")
scr.onkey(down, "s")
scr.onkey(right, "d")

scr.onkey(p_up, "space")

scr.onkey(ch_s, "1")
scr.onkey(ch_c, "2")

scr.onkey(fill, "q")
scr.onkey(e_fill, "e")

scr.onkey(p.stamp, "t")

scr.onkey(reset, "r")
scr.onkey(end, "Escape")


while 1:
    try:
        p.forward(speed)        # speed 만큼 계속 직진
    except:
        print("종료합니다.")    # end 실행으로 인한 오류 발생시 종료 문구 출력
        break
