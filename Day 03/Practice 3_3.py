li = []

while 1:
    try:
        a = input("\n원하는 숫자를 입력해주세요. ( 입력종료 시 END 입력 )    :    ")
        li.append(int(a))
        print("\n>>\t현재 입력된 숫자     :    ", li)
    except:
        if (a.upper() == "END"):
            break
        else:
            print("\n계속 입력을 원할 시 숫자, 종료를 원하시면 END 만 입력해주세요.\n")

Max = li[0]
Min = li[0]

for i in range(len(li)):
    if ( li[i] >= Max ):
        Max = li[i]
    if ( li[i] <= Min ):
        Min = li[i]
            
print("\n\n>>\t최대값 =", Max)
print(">>\t최소값 =", Min,"\n")

print("\n종료합니다.")
