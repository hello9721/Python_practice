# Q. str의 /로 구분된 각각의 옵션 추출 및 PZ 옵션의 값을 x, y, w, h 로 구분하여 표기

# 입력된 문자열
str = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"

str_sp = str.split("/")            # 옵션별로 구분

ps = str_sp[1].split(":")         # PS의 값 추출
pz = str_sp[2]                  # PZ의 값 추출
file = str_sp[3].split("=")       # FILE의 값 추출

pz_sp = pz[3: ].split(",")       # PZ의 값을 x, y, w, h 구분하여 추출

print(f"{file[0]} = {file[1]}\n{ps[0]} = {ps[1]}\n{pz[ :2]}.X = {pz_sp[0]}\n{pz[ :2]}.Y = {pz_sp[1]}\n{pz[ :2]}.W = {pz_sp[2]}\n{pz[ :2]}.H = {pz_sp[3]}")

# 결과값
# FILE = test.py
# PS = 121 
# PZ.X = 2
# PZ.Y = 3
# PZ.W = 100
# PZ.H = 100 


# Q. PS의 값만을 반환하는 함수 

def get_PS(s):
    s_sp = s.split(":")
    return s_sp[1]

s= "/PS:121"

print(get_PS(s))

# 결과값
# 121


# Q. PZ의 값만을 반환하는 함수 

def get_PZ(s):
    s_sp = s.split(":")
    s_list = s_sp[1].split(",")
    return s_list

s= "/PZ:2,3,100,100"

print("x =", get_PZ(s)[0], ", y =", get_PZ(s)[1], ", w =", get_PZ(s)[2], ", h =", get_PZ(s)[3])

# 결과값
#x = 2 , y = 3 , w = 100 , h = 100


# 참고 지식
# "\r" CR(커서를 맨 앞으로 되돌리기) / "\n" LF(종이를 한 칸 올리기)
# c:\user\temp\test.py => \u로 인해 오류 / \t는 탭으로 인식
# \ -> / 로 해주거나 \\ 사용하기
