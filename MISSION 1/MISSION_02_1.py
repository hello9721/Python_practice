# Q2 수학 함수를 이용하여 그리기 -> sin/ 원 / 원 안의 sin

import math as m

str = "●"

# sin 그래프
# sin = m.sin(m.pi*(degree/180))

sin_lst = [0] * 46                  # sin 수치 값이 담길 리스트
sin_cnt = [0] * 19                  # sin 수치 값의 빈도수가 담길 리스트

for i in range(1, 46):              
    
    s = int ( m.sin(m.pi * ( i * 8 / 180 )) * 10 )
                                    # 간소화를 위해 0도부터 360도까지, 361개를
                                    # (0 * 8)도부터 (45 * 8)도까지, 46개로 표시하고
                                    # 소수점 1자리 까지를 정수로 표현
    sin_lst[i] = s + 9              # -9 ~ 9 이지만 표현하기 쉽게 하기위해
    sin_cnt[s + 9] += 1             # +9 를 해서 전부 양수화
    


for i in range(19):                 # cnt의 수만큼 반복

    i = 18 - i                      # 제일 위쪽부터 출력해야하기에 i = 18-i
    n = sin_cnt[i]                  # n에는 i의 빈도수

    a = 1                           
    lst = sin_lst[a: ]              
    
    while n != 0:                   # 반복이 진행될때마다 n은 1씩 줄어든다.
        
        ind = lst.index(i)          # ind에는 lst에서의 i의 인덱스번호

        print(f"{'  ' * ind}{str}", end = "")
                                    # 인덱스 번호만큼의 공백을 넣어주고 문자 출력
                                    # 같은 i끼리는 한줄에 쓰여야 하기 때문에 end = ""
        n -= 1
        a = ind + 1                 # ind는 이미 쓰였기때문에 a = ind+1
        lst = lst[a: ]              # 그리고 lst는 lst의 a부터 시작한다.
    
    print("")                       # 다른 i끼리는 다른 줄에 쓰기 위해 줄바꿈


# 원 그리기
# 원 위의 점 (x,y)
# 원 중앙의 점 (a,b)
# x = a + r * cos(dgr)
# y = b + r * sin(dgr)
# sin 그래프의 길이가 45
# == r = 22.5
# a == b == r

r = 22.5

x_t_lst = []                        # 위 반원
x_b_lst = []

y_t_lst = []                        # 아래 반원
y_b_lst = []

for i in range(46):

    s = m.sin(m.pi * ( i * 8 / 180 ))
    c = m.cos(m.pi * ( i * 8 / 180 ))
                                    # 간편하게 표현 하기 위해 올림
    if i < 23:                      # 위 반원
        x_t_lst.append(int(22.5 + r * c))
        y_t_lst.append(m.ceil(22.5 + r * s))
    else:                           # 아래 반원
        x_b_lst.append(int(22.5 + r * c))
        y_b_lst.append(m.ceil(22.5 + r * s))

check_t = list(set(y_t_lst))        # 중복 없는 체크 리스트
check_b = list(set(y_b_lst))

check_t.sort()                      # 가장 위부터 출력하기 위해 정렬
check_b.sort()
    
for i in range(len(check_t)):       # 위 체크리스트 갯수만큼

    i = len(check_t) - i - 1        # 리스트의 맨 뒤 요소부터
    n = y_t_lst.count(check_t[i])   # 요소의 빈도수 체크
    
    a = 0                           
    lst = y_t_lst[a: ]
    
    while n != 0:
        
        ind = lst.index(check_t[i]) # 요소의 인덱스
        if a == 0: print(f"{'  ' * x_t_lst[ind]}{str}", end = "")
                                    # 처음에는 해당 인덱스의 x요소만큼 공백추가
        else: print(f"{str}", end="")
                                    # 빈도수 만큼 출력
        n -= 1                      # n이 1씩 줄어들고 0이 되면 break
        a = ind + 1                 # 같은 부분을 다시 출력하지 않기 위해
        lst = lst[a: ]              
    
    print("")


for i in range(len(check_b)):       # 나머지 반원

    i = len(check_b) - i - 1
    n = y_b_lst.count(check_b[i])
    
    a = 0                           
    lst = y_b_lst[a: ]              
    
    while n != 0:
        
        ind = lst.index(check_b[i])
        if a == 0: print(f"{'  ' * x_b_lst[ind]}{str}", end = "")
        else: print(f"{str}", end="")

        n -= 1
        a = ind + 1
        lst = lst[a: ]
    
    print("")


# 원 안의 sin 그래프 (태극)
# 문자열로 구현하는 것은 포기

import matplotlib.pyplot as p
import numpy as n

a = n.arange(0, 360)                # 0부터 360까지
y = n.sin(n.radians(a)) * 60        # sin그래프는 -1부터 1까지 이므로 *60을 해서 y범위를 늘려줌

cx = [0] * 361
sy = [0] * 361

for i in range(1,361):              # 원 그리기
    cx[i] = 180 + 180 * m.cos(m.pi * i / 180)
    sy[i] = 0 + 180 * m.sin(m.pi * i / 180)

p.plot(cx, sy)
p.plot(y)

p.show()
