import requests

def save_img(url, file_name): # 이미지 저장 함수

    img = requests.get(url)
    
    with open("./ASSETS/" + file_name, "wb") as f:
        
        f.write(img.content)
        
# 챔피언 정보 데이터

url = "https://ddragon.leagueoflegends.com/cdn/12.21.1/data/ko_KR/champion.json"

req = requests.get(url)
js = req.json()

KEY = list(js["data"].keys())

n = len(KEY)

URL = [""] * n
NAME = [""] * n
TITLE = [""] * n
DIFFICULTY = [""] * n
TAG = [""] * n
ADM = [""] * n
LANE = [""] * n
LECTURE = [""] * n

Q = [""] * n
W = [""] * n
E = [""] * n
R = [""] * n



##f = open("./Lane_Info.csv") # 챔피언 별 라인 데이터
##
##t = []
##lane = []
##
##for i in f:
##
##    lane.append(i.split(",")[0])
##    t.append(i.upper().strip().split(",")[1: ])
##
##f.close()        
##
##for i in range(n):
##
##    temp = []
##
##    for j in range(len(lane)):
##    
##        if KEY[i].upper() in t[j]:
##
##            if len(temp) <= 2:
##
##                temp.append(lane[j])
##
##    if len(temp) == 1:
##
##        temp.append("-")
##
##    LANE[i] = temp


for i in range(n): # 서버에서 챔피언별 데이터 가져오기

##    URL[i] = f"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/{KEY[i]}_0.jpg"
##    NAME[i] = js["data"][KEY[i]]["name"]
##    TITLE[i] = js["data"][KEY[i]]["title"]
##    DIFFICULTY[i] = js["data"][KEY[i]]["info"]["difficulty"]
##    TAG[i] = js["data"][KEY[i]]["tags"]
##    ADM[i] = [ js["data"][KEY[i]]["info"]["attack"], js["data"][KEY[i]]["info"]["defense"], js["data"][KEY[i]]["info"]["magic"] ]

    url = f"https://ddragon.leagueoflegends.com/cdn/12.21.1/data/en_US/champion/{KEY[i]}.json"

    req = requests.get(url)
    js = req.json()

    print(KEY[i])
    try:
        Q[i] = js["data"][KEY[i]]["spells"][0]["tooltip"].split("<status>")[1].split("</status>")[0].upper()
    except:
        Q[i] = "-"
        
    try:
        W[i] = js["data"][KEY[i]]["spells"][1]["tooltip"].split("<status>")[1].split("</status>")[0].upper()
    except:
        W[i] = "-"

    try:
        E[i] = js["data"][KEY[i]]["spells"][2]["tooltip"].split("<status>")[1].split("</status>")[0].upper()
    except:
        E[i] = "-"

    try:
        R[i] = js["data"][KEY[i]]["spells"][3]["tooltip"].split("<status>")[1].split("</status>")[0].upper()
    except:
        R[i] = "-"


for i in range(n):

    if "FEAR" in Q[i]: Q[i] = "FEAR"
    if "GROUND" in Q[i]: Q[i] = "GROUND"
    if "IMMOBILIZ" in Q[i]: Q[i] = "IMMOBILIZE"
    if "KNOCK" in Q[i]: Q[i] = "KNOCK"
    if "PULL" in Q[i]: Q[i] = "PULL"
    if "ROOT" in Q[i]: Q[i] = "ROOT"
    if "SLOW" in Q[i]: Q[i] = "SLOW"
    if "STUN" in Q[i]: Q[i] = "STUN"
    if "SUPPRESS" in Q[i]: Q[i] = "SUPPRESS"
    if "TAUNT" in Q[i]: Q[i] = "TAUNT"

    if "AIRBORNE" in Q[i]: Q[i] = "-"
    if "ASLEEP" in Q[i]: Q[i] = "-"
    if "BERSERKING" in Q[i]: Q[i] = "-"
    if "BLINDING" in Q[i]: Q[i] = "-"
    if "DISARMED" in Q[i]: Q[i] = "-"
    if "DROWSY" in Q[i]: Q[i] = "-"
    if "POLYMORPHS" in Q[i]: Q[i] = "-"

for i in range(n):

    if "FEAR" in W[i]: W[i] = "FEAR"
    if "GROUND" in W[i]: W[i] = "GROUND"
    if "IMMOBILIZ" in W[i]: W[i] = "IMMOBILIZE"
    if "KNOCK" in W[i]: W[i] = "KNOCK"
    if "PULL" in W[i]: W[i] = "PULL"
    if "ROOT" in W[i]: W[i] = "ROOT"
    if "SLOW" in W[i]: W[i] = "SLOW"
    if "STUN" in W[i]: W[i] = "STUN"
    if "SUPPRESS" in W[i]: W[i] = "SUPPRESS"
    if "TAUNT" in W[i]: W[i] = "TAUNT"

    if "AIRBORNE" in W[i]: W[i] = "-"
    if "ASLEEP" in W[i]: W[i] = "-"
    if "BERSERKING" in W[i]: W[i] = "-"
    if "BLINDING" in W[i]: W[i] = "-"
    if "DISARMED" in W[i]: W[i] = "-"
    if "DROWSY" in W[i]: W[i] = "-"
    if "POLYMORPHS" in W[i]: W[i] = "-"

for i in range(n):

    if "FEAR" in E[i]: E[i] = "FEAR"
    if "GROUND" in E[i]: E[i] = "GROUND"
    if "IMMOBILIZ" in E[i]: E[i] = "IMMOBILIZE"
    if "KNOCK" in E[i]: E[i] = "KNOCK"
    if "PULL" in E[i]: E[i] = "PULL"
    if "ROOT" in E[i]: E[i] = "ROOT"
    if "SLOW" in E[i]: E[i] = "SLOW"
    if "STUN" in E[i]: E[i] = "STUN"
    if "SUPPRESS" in E[i]: E[i] = "SUPPRESS"
    if "TAUNT" in E[i]: E[i] = "TAUNT"

    if "AIRBORNE" in E[i]: E[i] = "-"
    if "ASLEEP" in E[i]: E[i] = "-"
    if "BERSERKING" in E[i]: E[i] = "-"
    if "BLINDING" in E[i]: E[i] = "-"
    if "DISARMED" in E[i]: E[i] = "-"
    if "DROWSY" in E[i]: E[i] = "-"
    if "POLYMORPHS" in E[i]: E[i] = "-"

for i in range(n):

    if "FEAR" in R[i]: R[i] = "FEAR"
    if "GROUND" in R[i]: R[i] = "GROUND"
    if "IMMOBILIZ" in R[i]: R[i] = "IMMOBILIZE"
    if "KNOCK" in R[i]: R[i] = "KNOCK"
    if "PULL" in R[i]: R[i] = "PULL"
    if "ROOT" in R[i]: R[i] = "ROOT"
    if "SLOW" in R[i]: R[i] = "SLOW"
    if "STUN" in R[i]: R[i] = "STUN"
    if "SUPPRESS" in R[i]: R[i] = "SUPPRESS"
    if "TAUNT" in R[i]: R[i] = "TAUNT"

    if "AIRBORNE" in R[i]: R[i] = "-"
    if "ASLEEP" in R[i]: R[i] = "-"
    if "BERSERKING" in R[i]: R[i] = "-"
    if "BLINDING" in R[i]: R[i] = "-"
    if "DISARMED" in R[i]: R[i] = "-"
    if "DROWSY" in R[i]: R[i] = "-"
    if "POLYMORPHS" in R[i]: R[i] = "-"



        
##f = open("./Lecture_Link.csv") # 챔피언별 강의 링크 데이터
##
##for i in f:
##
##    i = i.strip().split(",")
##
##    for j in range(n):
##
##        if i[0] == NAME[j]:
##
##            LECTURE[j] = i[1]
##
##f.close()
        

##f = open("./Champion_Data.csv", "w") # 필요 데이터 한파일에 모아 저장
##
##f.write("KEY, TITLE, NAME, DIFFICULTY, LANE1, LANE2, TAG1, TAG2, ATTACK, DEFENSE, MAGIC, IMG, LECTURE\n")
##
##for i in range(n):
##
##    if len(TAG[i]) == 1: f.write(f"{KEY[i]}, {TITLE[i]}, {NAME[i]}, {DIFFICULTY[i]}, {LANE[i][0]}, {LANE[i][1]}, {TAG[i][0]}, -, {ADM[i][0]}, {ADM[i][1]}, {ADM[i][2]}, {URL[i]}, {LECTURE[i]}\n")
##    else: f.write(f"{KEY[i]}, {TITLE[i]}, {NAME[i]}, {DIFFICULTY[i]}, {LANE[i][0]}, {LANE[i][1]}, {TAG[i][0]}, {TAG[i][1]}, {ADM[i][0]}, {ADM[i][1]}, {ADM[i][2]}, {URL[i]}, {LECTURE[i]}\n")
##
##f.close()

f = open("./Champion_Skill.csv", "w")

f.write("KEY, Q, W, E, R\n")

for i in range(n):

    f.write(f"{KEY[i]}, {Q[i]}, {W[i]}, {E[i]}, {R[i]}\n")

f.close()

##for i in range(n): # 이미지 저장
##
##    save_img(URL[i], "CHAM_LONG/"+ KEY[i] + ".png")
##    save_img(f"http://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/{KEY[i]}.png", "/CHAM_SHORT/"+ KEY[i] + ".png")
##
