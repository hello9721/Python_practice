# 터틀 패키지
# 최소 1개의 클래스
# 함수 정의 및 사용
# 데이터 파일 사용

from P_16_1_df import *

t.setworldcoordinates(-600, -200, 600, 1000)        # 스크린 크기 설정
                                                    # x, y / 그릴모양 /  width, height
                                                    # 형식으로 작성된 텍스트파일 불러오기
f = open("./data/squid.txt")

for i in f:

    if i.strip() == "delete":                       # delete 가 들어온다면
                                                    # 다음 i 부터 하얀 색으로 지우기 모드
        a = point(0, 0)
        a.pen("white", 2)

    elif i.strip() == "draw":                       # draw 가 들어온다면
                                                    # 다음 i 부터 검은 색으로 그리기 모드
        a = point(0, 0)
        a.pen("black", 1)

    else:                                           # 그외의 내용이라면
        
        temp = i.split("/")                         # / 를 구분자로 분리
        
        x, y = map(int, temp[0].strip().split(", "))# x, y는 첫 요소를 , 로 분리
        w, h = map(int, temp[2].strip().split(", "))# w, h는 마지막 요소를 , 로 분리
    
        a = draw(x, y)                              # 임시 변수 a로 객체화

        if temp[1].strip() == "s": a.sq(w, h)       # 두번째 요소가 s 일 때
                                                    # 현재 위치 중심으로 사각형 그리기
        elif temp[1].strip() == "t": a.tr(w, h)     # t 일 때
                                                    # 현재 위치 중심으로 삼각형
        elif temp[1].strip() == "c": a.cir(w, h)    # c 일 때
                                                    # 현재 위치 중심으로 원
        elif temp[1].strip() == "l": a.line(w, h)   # 현재 위치를 오른쪽 끝으로 하고
                                                    # 왼쪽 방향으로 직선 그리기

f.close()                                           # 파일 닫
