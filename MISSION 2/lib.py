import requests as re
import sqlite3 as sq

class summoner:

    api_key = "RGAPI-ad3cc2f9-014c-435a-8ad1-fd7ec6257bd3"
    platform_url = "https://kr.api.riotgames.com/"
    region_url = "https://asia.api.riotgames.com/"

    player_info = ""
    match_player_info = []

    process = 0

    def __init__(self, name):

        self.name = name

        url = self.platform_url + "lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + self.api_key

        request = re.get(url)
        self.player_info = request.json()

    def load_match_data(self):

        url = self.region_url + f"lol/match/v5/matches/by-puuid/{self.player_info['puuid']}/ids?start=0&count=80" + "&api_key=" + self.api_key

        request = re.get(url)
        match_ids = request.json()
        cnt = 0

        for i in match_ids:
            
            url = self.region_url + f"lol/match/v5/matches/{i}" + "?api_key=" + self.api_key

            request = re.get(url)
            temp = request.json()

            for j in range(len(temp["info"]["participants"])):

                if temp["info"]["gameMode"] == "CLASSIC":
                    if temp["info"]["participants"][j]["summonerName"] == self.player_info['name']:

                        k = temp["info"]["participants"][j]["kills"]
                        d = temp["info"]["participants"][j]["deaths"]
                        a = temp["info"]["participants"][j]["assists"]
                        
                        select_data = [0] * 5

                        select_data[0] = i
                        select_data[1] = temp["info"]["participants"][j]["championName"]
                        select_data[2] = temp["info"]["participants"][j]["teamPosition"]
                        select_data[4] = temp["info"]["participants"][j]["win"]

                        if d == 0: select_data[3] = round((k + a) * 1.2, 2)
                        else: select_data[3] = round((k + a)/d, 2)
                        
                        self.match_player_info.append(select_data)

            cnt += 1
            self.process = cnt * 100 / 80
            print(self.process)

    def update_match_data(self):

        conn = sq.connect("./DB/Player_Data.db", isolation_level= None)
        cmd = conn.cursor()

        cmd.execute('''
            SELECT MATCH_ID FROM MATCH_DATA;
        ''')
        match_id = cmd.fetchall()

        for i in self.match_player_info:

            win = 0
            
            if i[4] : win = 1
            else: win = 0

            if i[0] not in match_id:

                   cmd.execute(f'INSERT INTO MATCH_DATA VALUES ("{i[0]}", "{i[1]}", "{i[2]}", {i[3]}, {win})')
                   cmd.fetchall()
