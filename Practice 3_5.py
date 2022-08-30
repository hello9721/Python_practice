
#입력

num = []
korean = []
math = []
english = []
try:
    while 1:
        try:
            a = int(input("\n\n학생번호 : "))
            if ( a != 0 ):
                num.append(a)
                
                b = int(input("\n국어 점수 : "))
                c = int(input("\n수학 점수 : "))
                d = int(input("\n영어 점수 : "))
                
                korean.append(b)
                math.append(c)
                english.append(d)
                continue
            else:
                break
        except ValueError:
            print("\n\n숫자로만 입력해주세요.")
            continue        
        

    #연산   


    ksum = 0
    msum = 0
    esum = 0
        
    print("\n\n")
        
    # 학생별 총점/평균
    for i in range(len(num)):
        ssum = int(korean[i]) + int(math[i]) + int(english[i])
        saverg = ssum/len(num)

        print( f"번호 : {num[i]} | 점수 총 합계 : {ssum} | 평균 : {saverg:.2f}\n")

        # 과목별 총점/평균
    for i in range(len(num)):
        ksum = ksum + korean[i]
        msum = msum + math[i]
        esum = esum + english[i]

    kaverg = ksum/len(num)
    maverg = msum/len(num)
    eaverg = esum/len(num)

    print(f"\n\n과목 : 국어 | 점수 총 합계 : {ksum} | 평균 : {kaverg:.2f}")
    print(f"\n과목 : 수학 | 점수 총 합계 : {msum} | 평균 : {maverg:.2f}")
    print(f"\n과목 : 영어 | 점수 총 합계 : {esum} | 평균 : {eaverg:.2f}")

    print("\n\n종료합니다.")



except ZeroDivisionError:
    print("아무것도 입력되지 않아 종료합니다.")
