a = input().upper()

start = ord("A")                    # 알파벳 시작인 a의 아스키코드번호
end = ord(a)                        # 입력받은 알파벳의 아스키코드번호

uni = []                            # 필요한 아스키번호를 받을 리스트

for i in range(start, end+1):

    uni.append(i)                   # a 부터 입력까지 리스트에 저장

for i in range(len(uni)):           # uni의 갯수만큼 반복

    j = len(uni) - i                # 갯수에서 i를 빼서 j에 저장

    print(' ' * (len(uni)-j), chr(uni[i]) * j, sep = "")
                                    # 문자가 j 만큼 출력이 되기에
                                    # 전체 길이에서 j 만큼 빼서 공백 추가 후 출력
