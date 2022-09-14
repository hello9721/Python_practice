    # font = Casacadia Code

    # 아스키 코드 테이블 만들기

dec = [0] * 128


for i in range(128):
    dec[i] = i


for i in dec:
    print(f"\t{'%3d'%i}  |  {'%02x'%i}  |  {chr(i)}")
