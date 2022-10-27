# SQL Interpreter 만들기

import sqlite3 as sq

con = sq.connect("C:/Users/user8/Documents/GitHub/Python_practice/Day 22/DB/P_22_1_DB.db")
cmd = con.cursor()

while 1:

    try:

        line = input("\n:: ")

        if line == "0":break

        cmd.execute(line)

        if line.split()[0] == "select":
    
            temp = cmd.fetchall()

            print("")

            for i in temp: print(i)

    except:

        print("\n다시 입력해주세요.")
        continue
