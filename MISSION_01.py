# Q1 0~100 난수 발행 후 파일에 과목별 점수 기록

import random                       # 난수 발생 패키지

class name:                         # lst 에서 임의의 이름을 중복 있게 뽑음
    
    name = ""

    def __init__(self, lst):
        random.shuffle(lst)

        self.name = lst[random.randrange(0, len(lst)-1 )]
    
class score(name):                  # name을 상속 받아서
    k = 0
    e = 0
    m = 0
    c = 0
    
    def random(self):
        random_score = [0] * 4      # 4 과목에 0부터 100 중 랜덤한 숫자를 뽑아 점수로 부여

        for i in range(4):
            random_score[i] = random.randrange(0, 101)

        self.k = random_score[0]
        self.e = random_score[1]
        self.m = random_score[2]
        self.c = random_score[3]

    def save(self, count):          # a 모드로 열고 데이터 넣기
        f = open("./result/score.csv", "a")

        if count == 0:
            f.write("이름,국어,영어,수학,컴퓨터\n")

        f.write(f"{self.name},{self.k},{self.e},{self.m},{self.c}\n")

        f.close()
        

# Main Routine


sample_name = ["배형욱", "전상은", "추용일", "표원정", "예하진", "서은일", "양시혁", "신은빈", "사공종환", "남원호", "신종우", "추영원", "문희용", "박혜훈", "정인석", "심만옥", "문호성", "봉은옥", "설도희", "추진희", "표대현", "최대일", "배동수", "안우정", "정효성", "고윤혜", "신윤정", "봉세희", "안선미", "유지태", "양지성", "풍윤호", "한정일", "남진아", "복신영", "추윤빈", "송해성", "허경진", "탁우민", "하주윤", "안영진", "제갈남기", "노진환", "박천화", "하광민", "정광수", "예민은", "강현철", "황보해남", "신성민"]

count = 0

for i in range(30):
    temp = score(sample_name)
    temp.random()
    temp.save(count)

    count += 1

print("저장 완료되었습니다.")        # 모든 과정이 완료되면 출력
            
