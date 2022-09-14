    # font = Casacadia Code
    
   
    # 문자열을 라인별로 받아서 16진수로 변환
    # 문자열 -> 10진수   # ord(c)
    # 10진수 -> 16진수   # {'%nx'%c} # n = 00 ~ 0F # n = 02/2 => 0a/a

file = open("test3.txt")

l = 1

for i in file:
    print(f" {'%3d'%l}\t{i}")
    print(f"\n   To hex {'-'*76}  >\n\n   ", end = "")

    count = 0
    
    for j in i:
        c = ord(j)
        
        print(f"{'%02x'%c} ", end = "")

        count += 1

        if count%29 == 0:
            print("\n   ", end = "")
            
        
    print("\n\n")
    
    l += 1
