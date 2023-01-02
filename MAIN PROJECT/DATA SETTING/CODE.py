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

f = open("CODE.csv", "w")                                   # 장비 코드가 저장될 파일

for i in table_name:                                        # 장비 코드를 하나씩 작성

    f.write(f"{i}, ")

f.close()
