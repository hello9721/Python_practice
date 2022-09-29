from itertools import *                  # 여러가지 경우의 수를 추출할 수 있는 라이브러리
import random as r                       # 가격설정을 위해 random import

f = open("./source/메뉴1.txt")           # 메뉴 이름 불러오기

for i in f: food = i.split("\n")[0].split(",")
                                         # food로 저장
price = []                               # 가격 리스트 생성

for i in range(len(food)): price.append(r.randrange(1000, 5000, 500))
                                         # 1000에서 5000 까지 500단위로 랜덤 생성
money = int(input("\n얼마 있으세요?\n")) # 손님이 가지고 계신 돈 입력 받기

many = int(input("\n몇 가지 품목을 원하세요?\n"))
                                         # 경우의 수가 많기에 출력하는 수를 줄이기 위해 원하는 갯수 입력
temp = list(combinations(food, many))    # 순서 상관 없이 중복 없는 조합을 list로 temp에 반환

cnt = 0                                  # pagination을 위해 cnt

while 1:                                 # 계속 반복
    try:
        page = cnt * 30                  # 한 페이지당 30개씩
        
        for i in range(30):              # 한 페이지에 temp의 0 ~ 29 / 30 ~ 59 / ...
            
            p = 0
            j = temp[i + page]
            
            for k in j:
                        
                p = p + price[food.index(k)]

            if (p < money) : print(f"\t구매 가능 하신 품목은 {j}, 총 가격은 {p} 원 입니다.\n")

        a = input(f"\t{cnt+1}/{len(temp)//30}\n\n다음 페이지를 보시겠어요? ( Y / N )\n\n")
                    
        if cnt == len(temp)//30:        # 모든 페이지가 열렸으면 종료

            print("\n종료합니다.")
            break
        
        if a.upper() != "Y":            # 사용자가 종료를 원하면 종료

            print("\n종료합니다.")
            break
        else: cnt += 1

    except:

        print("\n종료합니다.")          # 마지막 페이지가 남은 index에서 벗어나 오류가 생기면 종료
        break
