# Q5 입력받은 알파벳보다 하위 알파벳들 모두 출력

a = input().lower()

start = ord("a")                    # 알파벳 시작인 a의 아스키코드번호
end = ord(a)                        # 입력받은 알파벳의 아스키코드번호

uni = []                            # 필요한 아스키번호를 받을 리스트

for i in range(start, end+1):

    uni.append(i)                   # a 부터 입력까지 리스트에 저장

for i in range(len(uni)):

    i = len(uni) - i                # i는 len(uni) 부터 1까지

    for j in range(i):              # j는 1부터 i-1까지
    
        print(chr(uni[j]), end = "")# 줄바꿈이나 공백없이 uni[j]를 문자로 변환

    print("")                       # 줄바꿈
