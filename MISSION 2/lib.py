import requests as re
import sqlite3 as sq

import random as rn

# http://ddragon.leagueoflegends.com/cdn/12.21.1/img/profileicon/5024.png
# odOuObo
# Hide on bush

class summoner:

    api_key = "RGAPI-72893791-2df1-4f8c-ae70-5b9556054381"
    platform_url = "https://kr.api.riotgames.com/"
    region_url = "https://asia.api.riotgames.com/"

    player_info = ""
    
    tier = ""
    rank = ""
    wins = 0
    losses = 0
    
    match_player_info = []

    process = 0

    def input_data(self, name):

        self.name = name

        url = self.platform_url + "lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + self.api_key

        request = re.get(url)
        self.player_info = request.json()

    def load_match_data(self, progressBar):

        self.process = 0

        url = self.region_url + f"lol/match/v5/matches/by-puuid/{self.player_info['puuid']}/ids?start=0&count=80" + "&api_key=" + self.api_key

        request = re.get(url)
        match_ids = request.json()
        
        cnt = 0
        error = 0

        for i in match_ids:
            
            url = self.region_url + f"lol/match/v5/matches/{i}" + "?api_key=" + self.api_key

            request = re.get(url)
            temp = request.json()

            if request.status_code == 200:

                for j in range(len(temp["info"]["participants"])):

                    if temp["info"]["gameMode"] == "CLASSIC":
                        if temp["info"]["participants"][j]["summonerName"] == self.player_info['name']:

                            k = temp["info"]["participants"][j]["kills"]
                            d = temp["info"]["participants"][j]["deaths"]
                            a = temp["info"]["participants"][j]["assists"]
                            
                            select_data = [0] * 6

                            select_data[0] = i
                            select_data[1] = temp["info"]["participants"][j]["championName"]
                            select_data[2] = temp["info"]["participants"][j]["teamPosition"]
                            select_data[4] = f"{k}/{d}/{a}"
                            select_data[5] = temp["info"]["participants"][j]["win"]

                            if d == 0: select_data[3] = round((k + a) * 1.2, 2)
                            else: select_data[3] = round((k + a)/d, 2)
                            
                            self.match_player_info.append(select_data)
                            
            else: error += 1

            cnt += 1
            self.process = cnt * 100 / (len(match_ids) - error)
            
            progressBar.setProperty("value", self.process)

            print(self.process)

    def update_match_data(self):

        conn = sq.connect("./DB/Player_Data.db", isolation_level= None)
        cmd = conn.cursor()

        cmd.execute('''
            DELETE FROM MATCH_DATA
        ''')
        cmd.fetchall()

        for i in self.match_player_info:

            win = 0
            
            if i[4] : win = 1
            else: win = 0

            cmd.execute(f'INSERT INTO MATCH_DATA VALUES ("{i[0]}", "{i[1]}", "{i[2]}", {i[3]}, "{i[4]}", {win})')
            cmd.fetchall()

    def tier_data(self):

        id_ = self.player_info["id"]

        url = self.platform_url + f"lol/league/v4/entries/by-summoner/{id_}" + "?api_key=" + self.api_key

        request = re.get(url)
        temp = request.json()

        if temp == []:

            self.tier = "Unranked"
            self.rank = ""
            self.wins = "Unranked"
            self.losses = "Unranked"

        elif len(temp) == 2:

            self.tier = temp[1]["tier"]
            self.rank = temp[1]["rank"]
            self.wins = temp[1]["wins"]
            self.losses = temp[1]["losses"]

        else:

            self.tier = temp[0]["tier"]
            self.rank = temp[0]["rank"]
            self.wins = temp[0]["wins"]
            self.losses = temp[0]["losses"]

    def my_champ(self):

        conn = sq.connect("./DB/Player_Data.db", isolation_level= None)
        cmd = conn.cursor()

        cmd.execute('''
            SELECT CHAMPION FROM MATCH_DATA
        ''')
        use_champ = cmd.fetchall()

        for i in range(len(use_champ)):

            use_champ[i] = use_champ[i][0]

        my_champ = list(set(use_champ))
        my_cnt = [0] * len(my_champ)

        for i in use_champ:

            idx = my_champ.index(i)
            my_cnt[idx] += 1

        f = open("./DATA/Champion_Data.csv")

        my_champ_info = [""] * len(my_champ)
        temp = []

        for i in f:

            temp.append(i.split("\n")[0].split(","))

        temp = temp[1: ]

        for i in range(len(my_champ)):

            for j in temp:

                if my_champ[i] == j[0]:

                    my_champ_info[i] = j
        
        for i in range(len(my_champ_info)):

            line = f"( {my_cnt[i]}, "
            
            for j in my_champ_info[i]:

                line += f'"{j.strip()}", '

            line = line[ :len(line)-2] + " )"
            
            my_champ_info[i] = line
            
        cmd.execute('DELETE FROM MY_CHAMPION')
        cmd.fetchall()

        for i in my_champ_info:
            
            cmd.execute(f'INSERT INTO MY_CHAMPION VALUES ' + i)
            cmd.fetchall()

        f.close()

    def pick_champ(self, lst, key, dif):
        
        f = open("./DATA/Champion_Data.csv")

        champ = []
        
        for i in f:

            if key not in i:

                if lst[2] in i: champ.append(i.split("\n")[0].split(","))

        lane_champ = []

        for i in champ:

            if lst[0] == i[4].strip():

                for j in range(len(i)): i[j] = i[j].strip()

                lane_champ.append(i)

        pick = []

        for i in lane_champ:

            if int(i[3].strip()) in dif:

                for j in range(len(i)): i[j] = i[j].strip()
                
                pick.append(i)
                
        for i in pick:

            lane_champ.remove(i)

        f.close()
        
        return lane_champ, pick

    def pick_lane(self, lane, dif):

        conn = sq.connect("./DB/Player_Data.db", isolation_level= None)
        cmd = conn.cursor()

        cmd.execute(f'SELECT KEY FROM MY_CHAMPION WHERE LANE1 = "{lane}"')
        used_champ = cmd.fetchall()

        for i in range(len(used_champ)):

            used_champ[i] = used_champ[i][0]

        f = open("./DATA/Champion_Data.csv")

        pick = []
        champ = []

        cnt = 0
        
        for i in f:

            temp = i.split("\n")[0].split(",")

            if cnt != 0:

                if temp[0].strip() not in used_champ:

                    for j in range(len(temp)): temp[j] = temp[j].strip()

                    if lane == temp[4]:

                        if int(temp[3]) in dif: pick.append(temp)
                        else: champ.append(temp)

            cnt += 1

        return champ, pick

        
    def random_pick(self, pick, champ):

        result = []

        n = 2

        random = rn.randrange(1, 5)
        
        if len(pick) < 2:

            n = 2 - len(pick)

            for i in range(random): rn.shuffle(champ)

            for i in range(n):

                result.append(champ[i])

            n = len(pick)

        for i in range(random): rn.shuffle(pick)
        
        for i in range(n):

            result.append(pick[i])

        return result
