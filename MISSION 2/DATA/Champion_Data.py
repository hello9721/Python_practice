import requests

def save_img(url, file_name):

    img = requests.get(url)

    if img.status_code == 200:
        with open("./result/" + file_name, "wb") as fp:
            
            fp.write(img.content)
            
    else: print("ERROR : ", response.json())

url = "https://ddragon.leagueoflegends.com/cdn/12.21.1/data/ko_KR/champion.json"

req = requests.get(url)
js = req.json()

KEY = list(js["data"].keys())

n = len(KEY)

URL = [""] * n
NAME = [""] * n
DIFFICULTY = [""] * n
TAG = [""] * n
ADM = [""] * n


for i in range(n):

    URL[i] = f"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/{KEY[i]}_0.jpg"
    NAME[i] = js["data"][KEY[i]]["name"]
    DIFFICULTY[i] = js["data"][KEY[i]]["info"]["difficulty"]
    TAG[i] = js["data"][KEY[i]]["tags"]
    ADM[i] = [ js["data"][KEY[i]]["info"]["attack"], js["data"][KEY[i]]["info"]["defense"], js["data"][KEY[i]]["info"]["magic"] ]

f = open("./champion_data.csv", "w")

f.write("KEY, NAME, DIFFICULTY, TAG1, TAG2, ATTACK, DEFENSE, MAGIC, IMG\n")

for i in range(n):

    if len(TAG[i]) == 1: f.write(f"{KEY[i]}, {NAME[i]}, {DIFFICULTY[i]}, {TAG[i][0]}, -, {ADM[i][0]}, {ADM[i][1]}, {ADM[i][2]}, {URL[i]}\n")
    else: f.write(f"{KEY[i]}, {NAME[i]}, {DIFFICULTY[i]}, {TAG[i][0]}, {TAG[i][1]}, {ADM[i][0]}, {ADM[i][1]}, {ADM[i][2]}, {URL[i]}\n")

f.close()
