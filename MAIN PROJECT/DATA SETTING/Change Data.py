import sqlite3 as sql

f = open("221226_tb_meter_log.csv")                         # 데이터 파일 로드

con = sql.connect("Power_Data.db")                          # DB 연결
cmd = con.cursor()                                          # DB 파일은 미리 생성해놓음.

table_name = []                                             # 장비 코드 (= 테이블 이름) 가 들어갈 리스트

for i in f:                                                 # 파일 한줄씩 읽기
    
    name = i.split(",")[0]                                  # , 로 분리 후 첫번째열 (= 장비 코드) 만 추출
    
    if name not in table_name: table_name.append(name)      # 중복 방지를 위해 리스트에 없는 것을 확인하고 append
    
table_name = table_name[1: ]                                # 열 이름이 같이 들어왔기에 0번째의 열이름 드랍

f.close()                                                   # 데이터 파일 닫기

for i in table_name:                                        # 장비 코드 하나씩 꺼내기
    
    query = f"""
                CREATE TABLE '{i}' (
                	id TEXT,
                	power_value FLOAT,
                    updated TEXT
                );
            """                                             # 장비 코드를 이름으로 삼아 테이블 생성
    cmd.execute(query)
    cmd.fetchall()
    con.commit()
    
    cnt = 1                                                 # 진행사항 확인용 카운트

    
for i in table_name:                                        # 장비 코드 하나씩 꺼내기
    
    temp = []                                               # 반복문 내에서 사용할 임시리스트 생성
    
    last = 0                                                # 결측치를 대체할 마지막 값 저장될 변수 선언
    
    f = open("221226_tb_meter_log.csv")                     # 데이터 파일 열기
    
    for j in f:                                             # 데이터 한줄씩 읽기
        
        if last != 0:                                       # 첫 줄 (= 열 이름) 드랍
        
            j = j.split("\n")[0]                            # 마지막 줄바꿈부호 제거
            j = j.split(",")                                # , 를 기준으로 분리하여
            j[1] = float(j[1])
            
            time = j[2].split(" ")[1]                       # 하루 마지막 관측값만 추출하기 위하여 시간 부분 따로 변수에 저장
            
            if j[1] != 0: last = j[1]                       # 관측값이 0 이 아닐때 last 변수 갱신
            else: j[1] = last                               # 관측값이 0 이라면 0 인 관측값을 last 값으로 대체
            
            
            if i == j[0]:                                   # table 이름과 장비ID가 일치한다면
                
                if "23:" in time:                           # 그리고 시간을 따로 추출하여 저장한 time에 23시를 나타내는 '23:' 이 들어있다면
                            
                    query = f"INSERT INTO '{i}' VALUES ('{j[0]}', {j[1]}, '{j[2]}')"
                                                            # 데이터 추가
                    cmd.execute(query)
                    cmd.fetchall()
                    con.commit()
                
        else: last += 1                                     # 첫 줄 이후에는 else가 아닌 if의 조건을 만족하도록
                                                            # 임의로 +1
                                                            
    print(cnt)                                              # 한 테이블 완료할때마다 출력 및 +1
    cnt += 1
            
    f.close()                                               # 데이터 파일 닫기
            
cmd.close()                                                 # DB Disconnect
con.close()
            