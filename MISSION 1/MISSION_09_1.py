# Q9 음식 이름과 가격이 표시된 메뉴판에서 정해진 금액으로 가능한 모든 2가지 주문 조합을 나열

# 떡 이름 데이터와 random 함수로 가격을 뽑아 사용
# 가격 범위는 1000 ~ 5000 사이, step은 500
# 정해진 금액은 입력 받아 사용

import random as r                  # 가격설정을 위해 random import

f = open("./source/메뉴.txt")        # 메뉴 이름 불러오기

for i in f: food = i.split("\n")[0].split(",")
                                     # food로 저장
price = []                           # 가격 리스트 생성

for i in range(len(food)): price.append(r.randrange(1000, 5000, 500))
                                     # 1000에서 5000 까지 500단위로 랜덤 생성
money = int(input("얼마 있으세요?\n")) # 손님이 가지고 계신 돈 입력 받기
                                    
for i in range(len(food)):           # food의 길이 만큼 반복

    a = price[i]                     # a는 food[i] 가격이고

    for j in range(len(food)):       # 또 food 길이만큼 반복하지만

        if i != j:                   # i랑 j가 같지 않을때

            if a + price[j] < money: # 그리고 a에 food[j]의 가격을 더해도 가진 돈을 넘지 않을 때 

                a = a + price[j]     # a에 food[j]의 가격을 더하고

                print(f"{food[i]} + {food[j]} = {a}")
                                     # 조합과 가격 출력
