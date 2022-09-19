# 실습

# Student Class 작성하기

# Person Class와 Score Class를 작성하고
# 이를 이용하여 Student Class를 완성하세요.

# KBD 혹은 File 을 이용하여 학생의 이름과 학번, 성적 정보를 입력하고 이를 출력.

class person:                               # 이름, 나이, 학번을 받아 저장

    name = ""
    age = ""
    number = ""
    
    def __init__(self, name, age, number):
        
        self.name = name
        self.age = age
        self.number = number

class score(person):                        # person 클래스를 상속 받아 학번을 통해 성적 파일에서 성적을 조회 하여 저장

    k_score = ""
    m_score = ""
    e_score = ""

    mean = 0
    
    def search(self):
        
        file = open("./class_score.txt")    # 성적 파일 열기

        for i in file:
            
            try:                            # 조회하려는 학번이 없을 경우 오류 대비
                
                score = i.split(",")
                
                if self.number == score[0].split(":")[1]:
                    
                                            # 학번 조회
                                            
                    self.k_score = score[1].split(":")[1]
                    self.m_score = score[2].split(":")[1]
                    self.e_score = score[3].split(":")[1]

                    self.mean = (int(self.k_score) + int(self.m_score) + int(self.e_score))/3
                    
                                            # 평균 계산
            except:
                
                print("잘못된 학번입니다.")
                                    
        file.close()                        # 파일 닫기
        
class student(score):                       # score 클래스를 상속을 받아 person과 score의 정보를 모두 사용 가능.
    
    def print(self):                        # 입력받은 정보와 파일에서 조회한 정보를 출력
        
        print(f"\n\t이름 : {self.name}\n\t나이 : {self.age}\n\t학번 : {self.number}")
        print(f"\n\t국어 : {self.k_score}\n\t수학 : {self.m_score}\n\t영어 : {self.e_score}")
        print(f"\t평균 : {self.mean:.2f}")

    def save(self, count):                  # 출력된 정보들을 파일로 저장
        
        file = open("./Student_info.txt", "a")

        file.write(f"\n\n---> {count}\n")
        file.write(f"\n\t이름 : {self.name}\n\t나이 : {self.age}\n\t학번 : {self.number}\n")
        file.write(f"\n\t국어 : {self.k_score}\n\t수학 : {self.m_score}\n\t영어 : {self.e_score}\n")
        file.write(f"\t평균 : {self.mean:.2f}\n")

        file.close()

def Main():                                 # 메인 루틴

    count = 0                               # 조회 번호 부여 용도
    
    while 1:

        name = input("\n이름 : ")            # 이름에 0 입력시 종료

        if '0' in name:

            print("\n종료하겠습니다.\n")
            
            break
        
        age = input("나이 : ")
        number = input("학번 : ")

        count += 1
        
        info = student(name, age, number)   # info라는 변수에 클래스 선언
                                            # + ) 입력받은 정보 전달
        info.search()                       # 성적 조회
        info.print()                        # 정보 출력

        save = input("\n저장하시겠습니까? ( Y / N )\n>> ")
                                            # 저장 할 건지 안 할건지 입력받아서
        if save.upper() == "Y": info.save(count)
        else:

            print("\n종료하겠습니다.\n")
            
            break                           # 저장 혹은 종료

        
Main()                                      # 메인 루틴 실행
