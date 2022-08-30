score = []
while 1:
    try:
        a = input("\n점수를 입력해주세요. ( 입력종료 시 END 입력 )    :    ")
        score.append(int(a))
        print("\n>>\t현재 등록된 점수     :    ", score)
    except:
        if (a.upper() == "END"):
            break
        else:
            print("\n계속 입력을 원할 시 숫자, 종료를 원하시면 END 만 입력해주세요.\n")

count = 0
Sum = 0

for i in score:
    count += 1
    Sum = Sum + i

averg = Sum/count

print(f"\n\n총 학생 수 : {count}")
print(f"총 점수 합계 : {Sum}")
print(f"평균 : {averg:.2f}\n\n")
print("종료합니다.")
