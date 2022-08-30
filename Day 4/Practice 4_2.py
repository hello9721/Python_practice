# Q. 입력된 문자열을 단어당 맨앞글자만 대문자가 되도록

# 함수 정의
def change(word) :
    for i in range(len(word)):
        a = str(list(word[i])[0]).upper()              # 첫글자 대문자
        b = str("".join(list(word[i])[1: ])).lower()    # 나머지 글자 소문자
        word[i] = a+b
        
    print("\n다음으로 변환 되었습니다.\n------------>>\t", " ".join(word))

# 사용 환경
while 1:
    word = []
    word = input("\n변환할 문자를 입력하세요\n------------>>\t ").split()
    
    change(word)               # 함수 실행

    ask = input("\n계속 하시겠습니까? ( YES / NO )\n------------>>\t ")
    
    if ask.upper() == "YES":   # 사용자가 또 다른 입력을 원할 경우 다시 시작
        continue
    else:
        print("\n\n프로그램을 종료합니다. \n\n감사합니다.")
        break
