# 예상 출력 ( 초과시간, 주말근무 포함 시 )

"""
하루 근무 시간 : 9
주당 총 근무 일수 : 7
시급 : 9000
주당 주말 근무 일수 : 2
기본 급여 : 567000원 
주말 근무수당 : 162000원 
예상 주급 : 729000원
"""
while True:
    # 필요 데이터 받기

    hours = int(input("하루 근무 시간 : "))
    days = int(input("주당 총 근무 일수 : "))
    rate = int(input("시급 : "))
    week = int(input("주당 주말 근무 일수 : "))

    # 주말근무 없이 초과근무만

    if ( hours * days > 40 and week == 0 ) :
        pay = hours * rate * days
        ot_pay = 40 * rate + ( hours * days - 40 ) * ( rate * 1.5 )
        ot = ot_pay - pay
        month = ot_pay * 4
        
        print(f"기본 급여 : {int(pay)}원 \n추가 초과 수당 : {int(ot)}원 \n예상 주급 : {int(ot_pay)}원 \n예상 월급 : {int(month)}원")

    # 주말근무와 초과근무 둘다

    elif ( hours * days > 40 and week > 0 ) :
        pay = hours * rate * days
        ot_pay = 40 * rate + ( hours * days - 40 ) * ( rate * 1.5 ) + ( week * rate * hours)
        ot = ot_pay - pay
        w = week * rate * hours
        month = ot_pay * 4
        
        print(f"기본 급여 : {int(pay)}원 \n추가 초과 수당 : {int(ot)}원 \n주말 근무 수당 : {int(w)}원 \n예상 주급 : {int(ot_pay)}원 \n예상 월급 : {int(month)}원")

    # 초과근무 없이 주말근무만

    elif ( hours * days <= 40 and week > 0 ):
        pay = hours * rate * days
        ot_pay = hours * rate * days + ( hours * rate * week)
        w = week * rate * hours
        month = ot_pay * 4

        print(f"기본 급여 : {int(pay)}원 \n주말 근무 수당 : {int(w)}원 \n예상 주급 : {int(ot_pay)}원 \n예상 월급 : {int(month)}원")

    # 초과근무와 주말근무 둘다 없이

    else:
        pay = hours * rate * days
        month = pay * 4

        print(f"예상 주급 : {int(pay)}원 \n예상 월급 : {int(month)}원")
    
    end = input("\n\n계산이 더 필요하신가요? ( Y / N ) : ")
    
    # 반복 끝내기 ( 정해진 답 외의 답에서는 무조건 break )

    if ( end.upper() == "N" ):
        print( "\n\n이용해주셔서 감사합니다." )
        break
    elif ( end.upper() == "Y"):
        print("\n")
        continue
    else:
        print( f'\n\n"{end}" 는 잘못된 입력입니다. \n잘못된 입력으로 인해 종료됩니다.' )
        break
