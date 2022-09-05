# s = "PS:121"

# PS의 값만을 반환하는 함수 

def get_PS(s):
    x = s.split(":")
    return x[1]

s = "PS:121"

print("PS =", get_PS(s))

# s = "PZ:2,3,100,100"

# PZ의 값만을 반환하는 함수 

def get_PZ(s):
    s_sp = s.split(":")
    s_list = s_sp[1].split(",")
    return s_list

s= "/PZ:2,3,100,100"

print("x =", get_PZ(s)[0], ", y =", get_PZ(s)[1], ", w =", get_PZ(s)[2], ", h =", get_PZ(s)[3])


# s = "FILE = test.py"

# FILE의 값만을 반환하는 함수 

def get_FILE(s):
    x = s.split("=")
    return x[1]

s = "FILE = test.py"

print("FILE =", get_FILE(s))

# str = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"

# 메인 루틴

def Main(s):
    s_li = s.split("/")
    ps = get_PS(s_li[1])
    pz = get_PZ(s_li[2])
    file  = get_FILE(s_li[3])
    
    print(f"PS = {ps} | PZ = [ x = {pz[0]}, y = {pz[1]}, w = {pz[2]}, h = {pz[3]} ] | FILE = {file}")

str = "/PS:121 /PZ:2,3,100,100 /FILE=test.py"

Main(str)
