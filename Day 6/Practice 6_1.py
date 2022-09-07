    #b = ["a","b","c","b","d","a","a"]

def count_lst(b):
    c = {}
    for i in b:
       c[i] = c.get(i, 0) +1
    # get = i가 c에 있다면  c[i]의 값을 가져오고 없다면 0
    return c   

    # dictionary 를 이용하여 특정 구문의 단어 구성과 빈도수 분석하기
    # Writing programs (or programming) is a very creative and rewarding activity. You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem. This book assumes that everyone needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills.


    # 특수문자와 공백을 원하는 구분자로 대치해주는 함수

def toSep(p, s):
    
    str_punc = " ~!@#$%^&*()_+`-={}:\"<>?[];',./\\|"

    for i in str_punc:
        for j in range(len(p)):
            if i in p[j]:
                p[j] = p[j].replace(i, s)
    return p


    # 중복되는 요소를 없애고 정렬해주는 함수

def setAndSort(w):
    
    w = set(w)
    w = list(w)
    w.sort()
    return w


    # 메인 루틴

def Main():
    
    phrase = input().split(".")         # input으로 문자열 받기
    phrase = toSep(phrase, "*")

    word = []                           # 문장들 "*" 기준 split

    for j in phrase:
        temp = j.split("*")
        for i in temp:
            i = i.upper()
                  
            if i != " " and i != "":
                word.append(i)

    dict = {}                           # get 함수로 빈도수를 측정 & dict에 할당

    for i in word:
        dict[i] = dict.get(i,0) +1

    word = setAndSort(word)

    for i in word:                      # 포맷 지정 출력
        print(f"{i} ____ {dict[i]}")


Main()                                  # 실행
