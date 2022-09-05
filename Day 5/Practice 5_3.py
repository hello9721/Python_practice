# s = "PS:121"

# PS의 값만을 반환하는 함수 

def get_PS(s):
    x = s.split(":")
    return x[1]

# s = "PZ:2,3,100,100"

# PZ의 값만을 반환하는 함수 

def get_PZ(s):
    s_sp = s.split(":")
    s_list = s_sp[1].split(",")
    return s_list

# s = "FILE = test.py"

# FILE의 값만을 반환하는 함수 

def get_FILE(s):
    x = s.split("=")
    return x[1]

# str = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"
# str1 = "/PZ:2,8,109,110 /PS:150 /FILE=test1.py"
# str2 = "/FILE=test2.py /PZ:99,8,199,110 /PS:800"

# 메인 루틴

def Main(s):
    ps = get_PS(s[s.find("PS"): ].split("/")[0])
    pz = get_PZ(s[s.find("PZ"): ].split("/")[0])
    file  = get_FILE(s[s.find("FILE"): ].split("/")[0])
    
    print(f"PS = {ps} | PZ = [ x = {pz[0]}, y = {pz[1]}, w = {pz[2]}, h = {pz[3]} ] | FILE = {file}")

str = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"
str1 = "/PZ:2,8,109,110 /PS:150 /FILE=test1.py"
str2 = "/FILE=test2.py /PZ:99,8,199,110 /PS:800"

Main(str)
Main(str1)
Main(str2)
