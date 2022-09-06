#b = ["a","b","c","b","d","a","a"]
#c={}

#for i in b:
    #c[i] = c.get(i, 0) +1
    # get = i가 c에 있다면  c[i]의 값을 가져오고 없다면 0


# 예시 구문

#Writing programs (or programming) is a very creative and rewarding activity. You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem. This book assumes that everyone needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills.

# dictionary 를 이용하여 특정 구문의 단어 구성과 빈도수 분석하기

phrase = input().split(".")

word = []

# 문장들을 띄어쓰기로 나누기

for i in phrase:
    temp = i.split(" ")
    for j in temp:
        word.append(j)

dict = {}

# 소괄호와 콤마, 공백들을 제외한 단어들만 get 함수로 빈도수를 측정함과 동시에 dict에 넣기

for i in word:
    if "(" in i:
        temp = i.split("(")
        i = temp[1]
    elif ")" in i:
        temp = i.split(")")
        i = temp[0]
    elif "," in i:
        temp = i.split(",")
        i = temp[0]

    i = i.upper()
    
    if i != " " and i != "":
        dict[i] = dict.get(i,0) +1
    else: continue

# 출력을 위해 중복되는 단어를 없애고

word = set(word)
word = list(word)

# 소괄호와 콤마를 없애고 공백도 나오지 않게 한 뒤 포맷 지정

for i in word:
    if "(" in i:
        temp = i.split("(")
        i = temp[1]
    elif ")" in i:
        temp = i.split(")")
        i = temp[0]
    elif "," in i:
        temp = i.split(",")
        i = temp[0]

    i = i.upper()
    
    if i != " " and i != "":
        print(f"{i} ____ {dict[i]}")
    else: continue
