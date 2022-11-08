from urllib.request import urlopen as u
from bs4 import BeautifulSoup as b

pos = ["top", "jungle", "adc", "support", "mid"]
url = "https://www.op.gg/champions?region=global&tier=all&position="

top = []
jungle = []
adc = []
support = []
mid = []

cnt = 0

for i in pos:

    html = u(f"{url}{i}")
    ob = b(html, "html.parser")

    cham = ob.tbody.find_all("strong")
    
    if cnt == 0: top = cham
    elif cnt == 1: jungle = cham
    elif cnt == 2: adc = cham
    elif cnt == 3: support = cham
    elif cnt == 4: mid = cham

    cnt += 1

f = open("./DATA/Lane_Info.csv", "w")

f.write("top, ")

for i in top:
    
    i = str(i).split(">")[1]
    i = i.split("<")[0]
    f.write(f"{i}, ")

f.write("\n")

f.write("jungle, ")

for i in jungle:
    
    i = str(i).split(">")[1]
    i = i.split("<")[0]
    f.write(f"{i}, ")

f.write("\n")

f.write("adc, ")

for i in adc:

    i = str(i).split(">")[1]
    i = i.split("<")[0]
    f.write(f"{i}, ")

f.write("\n")

f.write("support, ")

for i in support:

    i = str(i).split(">")[1]
    i = i.split("<")[0]
    f.write(f"{i}, ")

f.write("\n")

f.write("mid, ")

for i in mid:

    i = str(i).split(">")[1]
    i = i.split("<")[0]
    f.write(f"{i}, ")

f.write("\n")

f.close()
