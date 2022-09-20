    # font = Casacadia Code

    # 아스키 코드 테이블 만들기

dec = [0] * 128


for i in range(128):
    dec[i] = i


for i in range(33):
    lst = [0, 9, 10, 28, 29, 30, 31, 32]
                        # 텍스트로 표현되지 않는 문자 코드
    if i in lst:
        print(f"     {'%3d'%i} | {'%02x'%i} |  ", end = "")
        print(f" |   {'%3d'%(i+32)} | {'%02x'%(i+32)} | {chr(i+32)}", end = "")
        print(f" |   {'%3d'%(i+64)} | {'%02x'%(i+64)} | {chr(i+64)}", end = "")
        print(f" |   {'%3d'%(i+96)} | {'%02x'%(i+96)} | {chr(i+96)}")
    else:
        print(f"     {'%3d'%i} | {'%02x'%i} | {chr(i)}", end = "")
        print(f" |   {'%3d'%(i+32)} | {'%02x'%(i+32)} | {chr(i+32)}", end = "")
        print(f" |   {'%3d'%(i+64)} | {'%02x'%(i+64)} | {chr(i+64)}", end = "")
        print(f" |   {'%3d'%(i+96)} | {'%02x'%(i+96)} | {chr(i+96)}")

