

###### ------- > score 클래스


class score:
    
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0

    total = 0
    mean = 0

# ------------ > 학번별 성적이 담긴 파일에서 학번에 맞는 성적 데이터 불러오기
    
    def fileToData(self, r, number):
        
        file = open(r)
        
        for i in file:
            if number in i:
                n, a, b, c, d = i.split("\n")[0].split(",")

                self.score1 = int(a)
                self.score2 = int(b)
                self.score3 = int(c)
                self.score4 = int(d)

# ------------ > 합계와 평균 구하기
    
    def total_mean(self):
        
        self.total = self.score1 + self.score2 + self.score3 + self.score4
        self.mean = self.total/4

# ------------ > 성적, 합계, 평균을 리스트에 넣어주기
    
    def dataToList(self, l, n):
        
        l.append([ n, self.score1, self.score2, self.score3, self.score4, self.total, self.mean ])

    
###### ------- > person 클래스


class person(score):

    name = ""
    age = ""
    phone = ""
    number = ""

# ------------ > 파일에서 정보들을 가져와 리스트에 저장

    def fileToList(self, l, r):
        
        file = open(r)

        for i in file:
            n, a, p, b = i.split("\n")[0].split(",")

            y = Student()
                        
            y.name = n
            y.age = a
            y.phone = p
            y.number = b
            
            l.append(y)
            # print(f"\n이름 : {n} | 나이 : {a} | 전번 : {p} | 학번 : {b}\n")
        
        file.close()
        

###### -------> Student 클래스
        

class Student(person):
    
# ------------ > 정보들 폼에 맞춰 출력

    def print(self, l, l2):
        
        print("")
        print("||------------------|-------------|-----------|--------------------||-----------|-----------|-----------|-----------|-----------|-------------||")
        print("||           NUMBER |        NAME |       AGE |            PHONE N.||    KOREAN |      MATH |   ENGLISH |   HISTORY |     TOTAL |        MEAN ||")
        print("||------------------|-------------|-----------|--------------------||-----------|-----------|-----------|-----------|-----------|-------------||")

        for i in l:
        
            name = i.name

            s1, s2, s3, s4, t, m = "","","","","",""
            

            for j in l2:
                if i.number == j[0]:
                    s1, s2, s3, s4, t, m = str(j[1]), str(j[2]), str(j[3]), str(j[4]), str(j[5]), j[6]             
            
            n = 10 - len(name)
            
            if name.upper() != name.lower(): n += 2

            print(f"|| {'%15s'%i.number[0:15]}  |{n * ' '}{i.name[0:10]} |       {'%3s'%str(i.age)[0:3]} |    {'%15s'%i.phone[0:15]} ||", end = "")
            print(f"       {'%3s'%s1[0:3]} |       {'%3s'%s2[0:3]} |       {'%3s'%s3[0:3]} |       {'%3s'%s4[0:3]} |", end = "")
            print(f"       {'%3s'%t[0:3]} |       {'%.2f'%m} ||")

            if i != l[-1]:
                print("||  ----------------|  -----------|  ---------|  ------------------||  ---------|  ---------|  ---------|  ---------|  ---------|  -----------||")
            
        print("||------------------|-------------|-----------|--------------------||-----------|-----------|-----------|-----------|-----------|-------------||")


# ------------ > 정보들 폼에 맞춰 저장

    def saveToFile(self, l, l2):
        
        file = open("./Student.txt", "w")
        
        file.write("\n")
        file.write("||------------------|-------------|-----------|--------------------||-----------|-----------|-----------|-----------|-----------|-------------||\n")
        file.write("||           NUMBER |        NAME |       AGE |            PHONE N.||    KOREAN |      MATH |   ENGLISH |   HISTORY |     TOTAL |        MEAN ||\n")
        file.write("||------------------|-------------|-----------|--------------------||-----------|-----------|-----------|-----------|-----------|-------------||\n")

        for i in l:

            # l2에서 성적 불러오기
            
            s1, s2, s3, s4, t, m = "","","","","",""
            

            for j in l2:
                if i.number == j[0]:
                    s1, s2, s3, s4, t, m = str(j[1]), str(j[2]), str(j[3]), str(j[4]), str(j[5]), j[6]
                    
            # 이름이 영어일때도 폼이 망가지지 않기 위해
            
            name = i.name

            n = 10 - len(name)
            
            if name.upper() != name.lower(): n += 2

            # 출력
            
            file.write(f"|| {'%15s'%i.number[0:15]}  |{n * ' '}{i.name[0:10]} |       {'%3s'%str(i.age)[0:3]} |    {'%15s'%i.phone[0:15]} ||")
            file.write(f"       {'%3s'%s1[0:3]} |       {'%3s'%s2[0:3]} |       {'%3s'%s3[0:3]} |       {'%3s'%s4[0:3]} |")
            file.write(f"       {'%3s'%t[0:3]} |       {'%.2f'%m} ||\n")

            if i != l[-1]:
                file.write("||  ----------------|  -----------|  ---------|  ------------------||  ---------|  ---------|  ---------|  ---------|  ---------|  -----------||\n")

        file.write("||------------------|-------------|-----------|--------------------||-----------|-----------|-----------|-----------|-----------|-------------||\n")

        file.close()

        print("\n----- > 저장이 완료되었습니다.\n")


###### -------> 메인 루틴


def Main():
    student = []
    score = []
    x = Student()

    # 학생 데이터 가져오기
    
    file = "./Student.csv"
    x.fileToList(student, file)    

    # 학번에 따른 성적 데이터 가져오기

    file = "./Score.csv"
    for i in student:
        x.fileToData(file, i.number)
        x.total_mean()
        x.dataToList(score, i.number)

    # 학생정보와 성적정보 출력
    
    x.print(student, score)
    x.saveToFile(student, score)


###### -------> 실행


Main()
