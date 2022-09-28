# Q3 임의로 주어진 문자열에 회문이 있는 경우 최대 회문의 길이 출력

def is_p(lst):                  # 함수 선언
    
    return lst == lst[ : : -1]  # 리스트와 거꾸로 리스트가 같은지 T/F 반환

str = input()                   # 입력된 단어 저장 
lst = []                        # 회문일 경우 단어의 길이가 들어갈 리스트

for i in range(len(str)):       # 단어의 길이만큼 반복

    for j in range(i+2, len(str)+1):
                                # i + 1 부터 단어의 길이 + 1 만큼 반복
        if is_p(str[i:j]): lst.append(len(str[i:j]))
                                # i부터 j까지의 문자열이 회문일 경우
                                # 길이를 리스트에 저장
                                
try: print(max(lst))            # 최고 길이 출력
except: print("회문이 없습니다.")  # 회문이 없어서 오류가 날 경우 회문이 없다고 출력
