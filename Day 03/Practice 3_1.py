print("구구단을 외자! 구구단을 외자!")

while 1:
    try:
        n = input("\n\n원하는 단의 숫자를 입력하세요! (문자 = 구구단표)__")
        # 입력받은 단만 출력
        print(f"\n\n\t{int(n)}단을 외워보자!\n\n")

        for j in range(9):
            b = j+1
            print(f"\t{int(n)} x {b} = {int(n)*b}")
    except:
        # 한번에 9단까지
        for i in range(1,9):
            a = i+1
            print(f"\n\n\t{a}단을 외워보자!\n\n")

            for j in range(9):
                b = j+1
                print(f"\t{a} x {b} = {a*b}")

    answer = input("\n\n다른 단을 원하세요? ( Y / N )__")
    if answer.upper() == "Y":
        continue
    else:
        print("\n\n구구단을 종료합니다.")
        break
