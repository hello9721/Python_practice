# x를 input에 받기

x = input("x : ")

# 하나하나 작성하는 방법

if x == "" :
    print("x를 입력해주세요.")
elif int(x) < 0 :
    print("1 이상의 수부터 입력해주세요.")
elif 0 < int(x) < 11 :
    print("1번째 그룹에 속합니다.")
elif 10 < int(x) <21 :
    print("2번째 그룹에 속합니다.")
elif 20 < int(x) <31 :
    print("3번째 그룹에 속합니다.")
elif 30 < int(x) <41 :
    print("4번째 그룹에 속합니다.")
elif 40 < int(x) <51 :
    print("5번째 그룹에 속합니다.")
elif 50 < int(x) <61 :
    print("6번째 그룹에 속합니다.")
elif 60 < int(x) <71 :
    print("7번째 그룹에 속합니다.")
elif 70 < int(x) <81 :
    print("8번째 그룹에 속합니다.")
elif 80 < int(x) <91 :
    print("9번째 그룹에 속합니다.")
elif 90 < int(x) <101 :
    print("10번째 그룹에 속합니다.")
else :
    print("100 이하의 수까지만 입력해주세요.")


# 하나하나 작성하는 방법 ( and 사용 )

if x == "" :
    print("x를 입력해주세요.")
elif int(x) < 0 :
    print("1 이상의 수부터 입력해주세요.")
elif 0 < int(x) and int(x) < 11 :
    print("1번째 그룹에 속합니다.")
elif 10 < int(x) and int(x) <21 :
    print("2번째 그룹에 속합니다.")
elif 20 < int(x) and int(x) <31 :
    print("3번째 그룹에 속합니다.")
elif 30 < int(x) and int(x) <41 :
    print("4번째 그룹에 속합니다.")
elif 40 < int(x) and int(x) <51 :
    print("5번째 그룹에 속합니다.")
elif 50 < int(x) and int(x) <61 :
    print("6번째 그룹에 속합니다.")
elif 60 < int(x) and int(x) <71 :
    print("7번째 그룹에 속합니다.")
elif 70 < int(x) and int(x) <81 :
    print("8번째 그룹에 속합니다.")
elif 80 < int(x) and int(x) <91 :
    print("9번째 그룹에 속합니다.")
elif 90 < int(x) and int(x) <101 :
    print("10번째 그룹에 속합니다.")
else :
    print("100 이하의 수까지만 입력해주세요.")

# 하나하나 작성하는 방법 ( elif를 쓰지 않고 )

try:
    if int(x) < 0 :
        print("1 이상의 수부터 입력해주세요.")
    if 0 < int(x) < 11 :
        print("1번째 그룹에 속합니다.")
    if 10 < int(x) <21 :
        print("2번째 그룹에 속합니다.")
    if 20 < int(x) <31 :
        print("3번째 그룹에 속합니다.")
    if 30 < int(x) <41 :
        print("4번째 그룹에 속합니다.")
    if 40 < int(x) <51 :
        print("5번째 그룹에 속합니다.")
    if 50 < int(x) <61 :
        print("6번째 그룹에 속합니다.")
    if 60 < int(x) <71 :
        print("7번째 그룹에 속합니다.")
    if 70 < int(x) <81 :
        print("8번째 그룹에 속합니다.")
    if 80 < int(x) <91 :
        print("9번째 그룹에 속합니다.")
    if 90 < int(x) <101 :
        print("10번째 그룹에 속합니다.")
    if 100 < int(x) :
        print("100 이하의 수까지만 입력해주세요.")
except:
    print("x를 입력해주세요.")

# while 반복문을 사용한 방법    

switch = True
a = 1
b = 11
up = 0
count = 1

while switch:
    if x == "" :
        print("x를 입력해주세요.")
        switch = False
    elif ( a + up ) <= int(x) < ( b + up ):
        print(f"{count}번째 그룹에 속합니다.")
        switch = False
    elif 100 < int(x) :
        print("100 이하의 수까지만 입력해주세요.")
        switch = False
    elif int(x) < 0 :
        print("1 이상의 수부터 입력해주세요.")
        switch = False
    else:
        up = up +10
        count = count + 1



# for 반복문을 사용한 방법

a2 = 1
b2 = 11
up2 = 0
count2 = 1

for  i in range(10):
    if x == "" :
        print("x를 입력해주세요.")
        break
    elif ( a2 + up2 ) <= int(x) < ( b2 + up2 ):
        print(f"{count}번째 그룹에 속합니다.")
        break
    elif 100 < int(x) :
        print("100 이하의 수까지만 입력해주세요.")
        break
    elif int(x) < 0 :
        print("1 이상의 수부터 입력해주세요.")
        break
    else:
        up2 = up2 +10
        count2 = count2 + 1
