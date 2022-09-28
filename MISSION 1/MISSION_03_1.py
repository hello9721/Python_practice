# Q3 임의로 주어진 문자열에 회문이 있는 경우 최대 회문의 길이 출력

def is_p(lst):                  # 함수 선언
    
    return lst == lst[ : : -1]  # 리스트와 거꾸로 리스트가 같은지 T/F 반환

str = input()                   # 문자열 받고
check = list(set(str))          # 중복 없앤 check 리스트 생성
lst = list(str)                 # 문자열을 lst로 생성

len_lst = []                    # 회문이 있을 경우 길이가 들어갈 리스트 생성

check.sort()                    # check 리스트 정렬

for i in check:                 # check에서 하나씩 꺼내서
    
    if lst.count(i) == 2:       # 만약 i가 lst에 2개 있다면
        
        a = lst.index(i)        # 첫번째 i의 인덱스와
        b = lst[a+1: ].index(i) + 2 + a
                                # 두번째 i의 인덱스에 1을 더하여 각각 a,b에 저장해서
        
        if is_p(lst[a:b]): len_lst.append(len(lst[a:b]))
                                # len_lst 에 길이 추가

    elif lst.count(i) > 2:      # i가 3 이상 있을 때

        n = lst.count(i)        # i의 빈도수를 n에 저장하고

        while n != 1:           # n이 1일때까지 1씩 빼면서 반복

            n -= 1

            a = lst.index(i)    # 첫번째 i 인덱스와
            b = lst[a+1: ].index(i) + 2 + a
                                # 두번째 i 인덱스 + 1 을 a,b에 저장
        
            if is_p(lst[a:b]):
                
                len_lst.append(len(lst[a:b]))
                                # a부터 b까지가 회문이면 길이 저장
                lst = lst[a+1:]
                                # lst를 a 이상부터
            else:
                
                if is_p(lst[a:b]):
                
                    len_lst.append(len(lst[a:b]))
                                
                    lst = lst[a+1:]

                else:

                    lst = lst[a+1:]
                                # 모든 문자열 확인 후
                    
try: print(max(len_lst))        # 최고 길이 출력
except: print("회문이 없습니다.")  # 없어서 오류가 날 경우 회문이 없다고 출력

# 같은 문자가 연속 2이상이 양쪽에 포함된 회문일 경우 인식을 못하지만 일단 여기까지
