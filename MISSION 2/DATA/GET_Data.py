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

f = open("./Lane_Info.csv") # 챔피언 별 라인 데이터

t = []
lane = []

for i in f:

    lane.append(i.split(",")[0])
    t.append(i.upper().strip().split(",")[1: ])

f.close()        

for i in range(n):

    temp = []

    for j in range(len(lane)):
    
        if KEY[i].upper() in t[j]:

            if len(temp) <= 2:

                temp.append(lane[j])

    if len(temp) == 1:

        temp.append("-")

    LANE[i] = temp


for i in range(n): # 서버에서 챔피언별 데이터 가져오기

    URL[i] = f"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/{KEY[i]}_0.jpg"
    NAME[i] = js["data"][KEY[i]]["name"]
    TITLE[i] = js["data"][KEY[i]]["title"]
    DIFFICULTY[i] = js["data"][KEY[i]]["info"]["difficulty"]
    TAG[i] = js["data"][KEY[i]]["tags"]
    ADM[i] = [ js["data"][KEY[i]]["info"]["attack"], js["data"][KEY[i]]["info"]["defense"], js["data"][KEY[i]]["info"]["magic"] ]

f = open("./Lecture_Link.csv") # 챔피언별 강의 링크 데이터

for i in f:

    i = i.strip().split(",")

    for j in range(n):

        if i[0] == NAME[j]:

            LECTURE[j] = i[1]

f.close()
        

f = open("./Champion_Data.csv", "w") # 필요 데이터 한파일에 모아 저장

f.write("KEY, TITLE, NAME, DIFFICULTY, LANE1, LANE2, TAG1, TAG2, ATTACK, DEFENSE, MAGIC, IMG, LECTURE\n")

for i in range(n):

    if len(TAG[i]) == 1: f.write(f"{KEY[i]}, {TITLE[i]}, {NAME[i]}, {DIFFICULTY[i]}, {LANE[i][0]}, {LANE[i][1]}, {TAG[i][0]}, -, {ADM[i][0]}, {ADM[i][1]}, {ADM[i][2]}, {URL[i]}, {LECTURE[i]}\n")
    else: f.write(f"{KEY[i]}, {TITLE[i]}, {NAME[i]}, {DIFFICULTY[i]}, {LANE[i][0]}, {LANE[i][1]}, {TAG[i][0]}, {TAG[i][1]}, {ADM[i][0]}, {ADM[i][1]}, {ADM[i][2]}, {URL[i]}, {LECTURE[i]}\n")

f.close()

##for i in range(n): # 이미지 저장
##
##    save_img(URL[i], "CHAM_LONG/"+ KEY[i] + ".png")
##    save_img(f"http://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/{KEY[i]}.png", "/CHAM_SHORT/"+ KEY[i] + ".png")
##
