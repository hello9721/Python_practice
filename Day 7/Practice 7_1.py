# file = open("test.txt")
# for i in file:                          # 줄 단위로 읽음
#    print(f"[{i.strip()}]")      # \n 없애기

    # UnicodeDecodeError: 'cp949' codec can't decode byte 0xe2 in position 548: illegal multibyte sequence
    # 텍스트 파일의 인코딩을 ANSI로 저장



    # 텍스트 파일을 불러와서 안에 있는 단어의 종류와 빈도수 조사

    # 특수문자와 공백을 원하는 구분자로 대치해주는 함수

def toSep(p, s):
    
    str_punc = " ~!@#$%^&*()_+`-={}:\"”“<>?[];'‘’,./\\|\n"

    for i in str_punc:
        if i in p:
            p = p.replace(i, s)
            
    return p


    # 중복되는 요소를 없애고 정렬해주는 함수

def setAndSort(w):
    
    w = set(w)
    w = list(w)
    w.sort()
    return w

    # 메인 루틴

def Main():
    file = open("test4.txt")              # Current Directory == 현재 편집중인 파일이 저장되어있는 장소
                                                      # 텍스트 파일을 열어 적용
    phrase = []
    
    for i in file:
        phrase.append(toSep(i, "*"))# 문장 하나하나 가져와서 toSep에 넣기

    word = []                  

    for j in phrase:
        temp = j.split("*")                 # 문장들 "*" 기준 split
        for i in temp:
            i = i.upper()
            if i != "":                            # 빈 요소들 제거
                word.append(i)

    dict = {}                             

    for i in word:
        dict[i] = dict.get(i,0) +1       # get 함수로 빈도수를 측정 & dict에 할당

    word = setAndSort(word)

    for i in word:                        
        print(f"{i} ____ {dict[i]}")   # 포맷 지정 출력


Main()                                          # 실행


