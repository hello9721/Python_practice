# Q8 임의의 파일을 이용해서 이름, 과목, 점수를 입력 받고 합계와 평균을 계산해서 석차를 구한 후 저장
# 1번의 파일 활용

f = open("./result/score.csv", "r")
                                # 파일을 열고

header = []                     # 파일이 가지고 있는 헤더가 들어갈 리스트

name = []                       # 이름 리스트
k = []                          # 국어 점수 리스트
m = []                          # 수학 점수 리스트
e = []                          # 영어 점수 리스트
c = []                          # 컴퓨터 점수 리스트

m_num = []                      # 평균과 학생의 INDEX가 들어갈 리스트

total = []                      # 점수 합계 리스트

cnt = 0                         # 인덱스 대용

for i in f:

    if cnt == 0:
        
        header = i.split("\n")[0].split(",")
        cnt += 1                # cnt가 0이라면 헤더에 헤더들을 넣고 cnt + 1
        
    else:

        temp = i.split("\n")[0].split(",")
                                # 임시 변수에 불러온 값 리스트를 넣고
        name.append(temp[0])    # 이름
        k.append(int(temp[1]))  # 국어점수
        m.append(int(temp[2]))  # 수학점수
        e.append(int(temp[3]))  # 영어점수
        c.append(int(temp[4]))  # 컴퓨터점수 입력

        total.append(k[cnt-1]+m[cnt-1]+e[cnt-1]+c[cnt-1])
                                # 각 점수 리스트에 들어간 값들을 더해 합계 입력
        m_num.append([total[cnt-1]/4, cnt-1])
                                # 합계리스트에 들어간 값으로 평균 계산
                                # 해당 학생의 INDEX를 입력
        cnt += 1

f.close()                       # 데이터 파일 닫기

header.append("합계")            # 헤더 리스트에 추가로 입력할 헤더들 추가
header.append("평균")
header.append("석차")

m_num.sort(reverse = True)      # 석차 계산을 위해 내림차순으로 평균 sort

f = open("./result/score_total_mean.csv", "w")
                                # 데이터들을 반환할 파일을 쓰기모드로 열고
for i in header:
                                # 첫 줄에 헤더들을 , 로 구분하여 입력
    f.write(f"{i},")


cnt = []

for i in range(len(name)):      # 데이터 수 만큼 반복

    f.write("\n")               # 줄바꿈 해주고

    mean = 0                    # 사용할 평균과 석차 변수를 미리 선언
    n = 0
    
    for j in m_num:             # 1등부터 꼴등까지 순서대로 정렬된 m_num에서
                                # 하나씩 꺼내와서
        if i == j[1]:           # i와 INDEX가 같을 때
            mean = j[0]         # 평균은 해당 j의 평균 값이고
            n = m_num.index(j)  # 석차는 해당 j의 인덱스 값 + 1
                                # 학생을 INDEX로 구분하기에 동명이인이 있어도 중복 안됨.

    f.write(f"{name[i]},{k[i]},{m[i]},{e[i]},{c[i]},{total[i]},{mean},{n + 1}")
                                # 데이터를 원하는 순서대로 ,로 구분하여 입력
f.close()                       # 모두 입력이 되었으면 파일 닫기

print("완료되었습니다.")
