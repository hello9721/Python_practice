# SQLite 는 파이썬에서 이용하기가 수월하다.

# PRAGMA table_info("table") 테이블 정보 -> DB Browser 에서
# select * from PRAGMA_table_info("table")

import sqlite3 as sq

con = sq.connect("C:/Users/user8/Documents/GitHub/Python_practice/Day 22/DB/P_22_1_DB.db")
# DB 연결

cmd = con.cursor()
# 명령어 창 연결

cmd.execute('select * from userdata')
# 버퍼에 수행 결과 저장
userData = cmd.fetchall()
# 버퍼의 내용 출력  그리고 비움

cmd.execute('select * from userdata')
# 버퍼에 수행 결과 저장
user1 = cmd.fetchone()
# 해당 내용의 첫줄 출력 그리고 해당 줄 비움
# 다음 실행에서는 다음 줄 출력

user2 = cmd.fetchone()
user3 = cmd.fetchone()
user4 = cmd.fetchone()
user5 = cmd.fetchone()
user6 = cmd.fetchone()


