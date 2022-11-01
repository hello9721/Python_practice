import sqlite3 as sq

f = open("./DATA/Log_data.txt", encoding="utf-8")
data = []

for i in f: data.append(i.split("\n")[0].split("\x02")[1].split("\x03"))

equi = []
sens = []
wind = []
temp = []
stat = []
date = []

cnt = 0

for i in data:

    if cnt == 0:

        equi.append(i[0][0:6])
        sens.append(int(i[0][10:14]))
        wind.append(int(i[0][14:18].strip()))
        temp.append(int(i[0][18:22].strip()))
        stat.append(int(i[0][22]))
        date.append(i[1])

        cnt += 1

    else: cnt = 0

f.close()

f = open("./DB/P_23_1_DB.db", "w")
f.close()

con = sq.connect("./DB/P_23_1_DB.db", isolation_level= None)
cmd = con.cursor()

cmd.execute('''
CREATE TABLE "LOG_DATA" (
	"EQUIP_CODE"	TEXT NOT NULL,
	"SENSOR_CODE"	INTEGER,
	"WIND"	INTEGER,
	"TEMP"	INTEGER,
	"STATUS_CODE"	INTEGER,
	"DATE"  TEXT
);
''')
cmd.fetchall()


for i in range(len(equi)):

    cmd.execute(f"INSERT INTO LOG_DATA VALUES ('{equi[i]}', {sens[i]}, {wind[i]}, {temp[i]}, {stat[i]}, '{date[i]}')")
    cmd.fetchall()

print("저장 완료되었습니다.")
