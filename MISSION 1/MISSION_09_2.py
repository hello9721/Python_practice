# Q9 음식 이름과 가격이 표시된 메뉴판에서 정해진 금액으로 가능한 모든 주문 조합을 나열

# 떡 이름 데이터와 random 함수로 가격을 뽑아 사용
# 가격 범위는 1000 ~ 5000 사이, step은 500
# 정해진 금액은 입력 받아 사용

import random as r                  # 가격설정을 위해 random import

f = open("./source/메뉴1.txt")         # 메뉴 이름 불러오기

for i in f: food = i.split("\n")[0].split(",")
                                     # food로 저장
price = []                           # 가격 리스트 생성

for i in range(len(food)): price.append(r.randrange(1000, 5000, 500))
                                     # 1000에서 5000 까지 500단위로 랜덤 생성
money = int(input("얼마 있으세요?\n")) # 손님이 가지고 계신 돈 입력 받기

for i in range(len(food)):          # 메뉴의 갯수만큼 반복

    for j in range(i+1, len(food)): # i의 다음부터 메뉴의 갯수만큼 반복

        if sum(price[i:j+1]) < money:
                                    # i 부터 j+1, 즉, j까지 가격을 더해서 가진 돈과 비교
            for k in range(len(price[i:j])):
                                    # 조건에 맞을 i부터 j-1까지를 하나씩 출력
                print(f"{food[i:j][k]} + ", end = "")

            print(f"{food[j]} = {sum(price[i:j+1])}") 
                                    # 마지막 요소와 총 가격까지 출력
