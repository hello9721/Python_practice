# PS의 값만을 반환하는 함수 

def get_PS(s):
    x = s.split(":")
    return x[1]

# PZ의 값만을 반환하는 함수 

def get_PZ(s):
    s_sp = s.split(":")
    s_list = s_sp[1].split(",")
    return s_list

# FILE의 값만을 반환하는 함수 

def get_FILE(s):
    x = s.split("=")
    return x[1]

# 구조적으로 비슷한 get_PS(s)와 get_FILE(s) 통합
# /xx(sep)value => xx에 따라 설정된 서로 다른 구분자를 통해 Value 추출

# 1

def get_Value(s):
    if s[ :2] == "PS":
        a = ":"
    elif s[ :2] == "FI":
        a = "="
    
    x = s.split(a)
    return x[1]

# 2

def getOptionValue(s, d):
    x = s.split(d)
    return x[1]
  
# 메인 루틴 1

def Main1(s):
    try:        
        ps = get_Value(s[s.find("PS"): ].split("/")[0])
        pz_ = get_PZ(s[s.find("PZ"): ].split("/")[0])
        file  = get_Value(s[s.find("FILE"): ].split("/")[0])
        pz = []

        ps = ps.strip()
        file = file.strip()
        
        for i in pz_:
            i = i.strip()
            pz.append(i)

        print(f"PS = {ps} | PZ = [ x = {pz[0]}, y = {pz[1]}, w = {pz[2]}, h = {pz[3]} ] | FILE = {file}")

    except IndexError:
        print("PS | PZ [ x, y, w, h ] | FILE 중 존재하지 않는 요소가 있어 표시 할 수 없습니다.")

# 메인 루틴 2

def Main2(s):
    try:
        s_sp = s.split("/")
        
        for i in s_sp:
            i = i.strip()
            if i[ :2] == "PS":
                ps = getOptionValue(i, ":")
            elif i[ :2] == "PZ":
                pz = get_PZ(i)
            elif i[ :2] == "FI":
                file = getOptionValue(i, "=")
                
        print(f"PS = {ps} | PZ = [ x = {pz[0]}, y = {pz[1]}, w = {pz[2]}, h = {pz[3]} ] | FILE = {file}")

    except IndexError:
        print("PS | PZ [ x, y, w, h ] | FILE 중 존재하지 않는 요소가 있어 표시 할 수 없습니다.")

# 결과 출력

str = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"
str1 = "/PZ:2,8,109,110 /PS:150 /FILE=test1.py"
str2 = "/FILE=test2.py /PZ:99,80,999,110 /PS:800"

Main1(str)
Main1(str1)
Main1(str2)

Main2(str)
Main2(str1)
Main2(str2)
