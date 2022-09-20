class person:

    name = ""
    age = 0
    phone = ""
    
    def __init__(self, name, age, phone):
        
        self.name = name                    
        self.age = age                      
        self.phone = phone

class student(person):
    
    number = ""
    

# 텍스트 파일을 열어 그 안의 데이터를 꺼내오기

l =[]
file = open("./Student.csv")

for i in file:
    n, a, p, b = i.split("\n")[0].split(",")
    
    x = student( n, a, p )
    x.number = b

    l.append(x)
    
    # print(f"\n이름 : {n} | 나이 : {a} | 전번 : {p} | 학번 : {b}\n")

file.close()


# 가져온 정보들 폼에 맞춰 출력
    
print("\n||------------------|-------------|-----------|--------------------||")
print("||           NUMBER |        NAME |       AGE |            PHONE N.||")
print("||------------------|-------------|-----------|--------------------||")

for i in l:

    name = i.name
    
    n = 10 - len(name)                  # f"{'%10s'%name}" 으로도 가능
    
    if name.upper() != name.lower(): n += 2

    print(f"|| {'%15s'%i.number[0:15]}  |{n * ' '}{i.name[0:10]} |       {'%3s'%str(i.age)[0:3]} |    {'%15s'%i.phone[0:15]} ||")
                                        # 정해진 자리수 이상을 작성해서 폼이 무너지지 않도록
                                        # 슬라이싱을 이용하여 최대 길이까지만 표시한다.
                                        # {i:ns} => 왼쪽 정렬
                                        # {'%ns'%i} => 오른쪽 정렬
                                        
print("||------------------|-------------|-----------|--------------------||")
