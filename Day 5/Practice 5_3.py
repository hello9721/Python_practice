# s = "/PZ:2,3,100,100"

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
