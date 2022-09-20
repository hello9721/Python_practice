weather = input("오늘의 날씨는 어떤가요? ( RAIN / SUNNY / ... )___").upper()

friends = ["길동", "길순", "길찬"]


for friend in friends:
    if weather == "RAIN":
        print(f"\n{friend}아! 오늘은 비오니까 우산 챙겨가!")
    elif weather == "SUNNY":
        print(f"\n{friend}아! 오늘은 자외선이 강하니까 썬크림을 발라야돼!")
    else:
        print(f"\n{friend}아! 좋은 하루 보내!")
