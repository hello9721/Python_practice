from GUI import *
from lib import *

from PyQt5.QtGui import QPixmap

# 마이크 바이슨


class connect(Ui_MainWindow, summoner):

    best_cnt_chmp = ""
    best_kda_chmp = ""
    
    best_cnt_lane = ""
    best_kda_lane = ""

    total_search_match = 0
    lane = [["탑", "TOP", "Top"], ["미드", "MID", "Mid"], ["원거리 딜러", "BOTTOM", "Bot"], ["서포터", "SUPPORT", "Support"], ["정글", "JUNGLE", "Jungle"]]

    
    def setUi(self, MainWindow):

        self.setupUi(MainWindow)

        self.btn__enter.clicked.connect(self.load_data)
        self.ln__input.returnPressed.connect(self.load_data)


    def load_data(self):

        try:

            self.process = 0

            name = self.ln__input.text()

            self.input_data(name)
            self.load_match_data(self.progressBar)
            self.update_match_data()

            self.show_result_user()
            self.show_result_champ()
            self.show_result_lane()
            self.show_reco_champ()
            self.show_reco_lane()

        except: self.statusbar.showMessage("1 ~ 2 분뒤에 다시 시도해주세요.")

        
    def show_result_user(self):

        self.tier_data()

        if self.tier == "Unranked":

            tier_t = self.tier
            tier = self.tier

        else:

            tier_t = self.tier + "-" + self.rank
            tier = self.tier[0] + self.tier[1: ].lower()

        self.tier = tier

        self.lbl__tier.setPixmap(QPixmap(f"./ASSETS/TIER/Emblem_{tier}.png"))
        self.lbl__tier_t.setText(tier_t)
        self.lbl__name.setText(self.player_info['name'])
        self.lbl__lvl.setText(f"LEVEL {self.player_info['summonerLevel']}")

        self.my_champ()

        conn = sq.connect("./DB/Player_Data.db", isolation_level= None)
        cmd = conn.cursor()

        cmd.execute('SELECT ATTACK FROM MY_CHAMPION')
        atk = cmd.fetchall()
        cmd.execute('SELECT DEFENSE FROM MY_CHAMPION')
        dfs = cmd.fetchall()
        cmd.execute('SELECT MAGIC FROM MY_CHAMPION')
        mgc = cmd.fetchall()
        cmd.execute('SELECT KDA_VAL FROM MATCH_DATA')
        kda = cmd.fetchall()
        cmd.execute('SELECT DIFFICULTY FROM MY_CHAMPION')
        diff = cmd.fetchall()

        if self.wins == "Unranked":

            wins = self.wins
            losses = self.losses
            total = "-"

            rate = 00.00

        else:

            wins = self.wins
            losses = self.losses
            total = wins + losses

            rate = round(wins * 100 / total, 2)

        a = len(atk)
        b = len(kda)

        self.total_search_match = b

        atk_mean = 0
        dfs_mean = 0
        mgc_mean = 0
        diff_mean = 0
        
        k_mean = 0
        d_mean = 0
        a_mean = 0

        for i in range(a):

            atk_mean += int(atk[i][0])
            dfs_mean += int(dfs[i][0])
            mgc_mean += int(mgc[i][0])
            diff_mean += int(diff[i][0])

        atk_mean = round(atk_mean/a, 2)
        dfs_mean = round(dfs_mean/a, 2)
        mgc_mean = round(mgc_mean/a, 2)
        diff_mean = round(diff_mean/a, 2)

        for i in range(b):

            temp = kda[i][0].split("/")
                
            k_mean += int(temp[0])
            d_mean += int(temp[1])
            a_mean += int(temp[2])

        k_mean = round(k_mean/b, 2)
        d_mean = round(d_mean/b, 2)
        a_mean = round(a_mean/b, 2)

        self.lbl__adm.setText(f"ATTACK {atk_mean} | DEFENSE {dfs_mean} | MAGIC {mgc_mean}")
        self.lbl__kda.setText(f"KILL {k_mean} | DEATH {d_mean} | ASSIST {a_mean}")
        self.lbl__ad.setText(f" AVERAGE DIFFICULTY {diff_mean} / 10.00")
        self.lbl__rate.setText(f"RATE {rate}%")

        if wins == "Unranked": self.lbl__sum.setText(f"승리 {wins} | 패배 {losses} | TOTAL {total}")
        else: self.lbl__sum.setText(f"승리 {wins:03d} | 패배 {losses:03d} | TOTAL {total:03d}")
        

    def show_result_champ(self):

        conn = sq.connect("./DB/Player_Data.db", isolation_level= None)
        cmd = conn.cursor()

        cmd.execute('SELECT CNT FROM MY_CHAMPION')
        cnt = cmd.fetchall()

        for i in range(len(cnt)): cnt[i] = cnt[i][0]

        best_cnt = cnt.index(max(cnt)) + 1

        cmd.execute(f'SELECT * FROM MY_CHAMPION WHERE ROWID = {best_cnt}')
        best_cnt_champ = cmd.fetchall()

        cmd.execute('SELECT KDA FROM MATCH_DATA')
        kda = cmd.fetchall()

        for i in range(len(kda)): kda[i] = float(kda[i][0])

        best_kda = kda.index(max(kda)) + 1

        cmd.execute(f'SELECT CHAMPION FROM MATCH_DATA WHERE ROWID = {best_kda}')
        kda_champ = cmd.fetchall()

        cmd.execute(f'SELECT * FROM MY_CHAMPION WHERE KEY = "{kda_champ[0][0]}"')
        best_kda_champ = cmd.fetchall()

        self.lbl__fname.setText(f"{best_cnt_champ[0][3]} | {best_cnt_champ[0][1].upper()}")
        self.lbl__fadm.setText(f"ATK {int(best_cnt_champ[0][9]):02d} | DFS {int(best_cnt_champ[0][10]):02d} | MGC {int(best_cnt_champ[0][11]):02d}")
        self.lbl__fd.setText(f"DIFFICULTY {int(best_cnt_champ[0][4]):02d}")
        self.lbl__fval.setText(f"PLAY COUNT / TOTAL : {best_cnt_champ[0][0]} / {len(kda)}")
        self.lbl__fcham.setPixmap(QPixmap(f"./ASSETS/CHAM_SHORT/{best_cnt_champ[0][1]}.png"))

        self.lbl__bname.setText(f"{best_kda_champ[0][3]} | {best_kda_champ[0][1].upper()}")
        self.lbl__badm.setText(f"ATK {int(best_kda_champ[0][9]):02d} | DFS {int(best_kda_champ[0][10]):02d} | MGC {int(best_kda_champ[0][11]):02d}")
        self.lbl__bd.setText(f"DIFFICULTY {int(best_kda_champ[0][4]):02d}")
        self.lbl__bval.setText(f"AVERAGE KDA : {max(kda)}")
        self.lbl__bcham.setPixmap(QPixmap(f"./ASSETS/CHAM_SHORT/{best_kda_champ[0][1]}.png"))

        self.best_cnt_chmp = best_cnt_champ[0]
        self.best_kda_chmp = best_kda_champ[0]
        
        

    def show_result_lane(self):

        conn = sq.connect("./DB/Player_Data.db", isolation_level= None)
        cmd = conn.cursor()

        cmd.execute(f'SELECT POSITION FROM MATCH_DATA')
        position = cmd.fetchall()

        cnt_lane = [0] * 6
        kda_lane = [[0, 0, 0]] * 6
        
        pos = ["TOP", "MIDDLE", "BOTTOM", "UTILITY", "JUNGLE", ""]

        for i in position:
            
            idx = pos.index(i[0])
            cnt_lane[idx] += 1

        ind1 = cnt_lane.index(max(cnt_lane[ :-1]))
        best_cnt_pos = self.lane[ind1]
        

        cmd.execute('SELECT KDA_VAL FROM MATCH_DATA')
        kda = cmd.fetchall()

        for i in range(len(kda)):

            idx = pos.index(position[i][0])

            kda[i] = kda[i][0].split("/")

            kda_lane[idx][0] += int(kda[i][0])
            kda_lane[idx][1] += int(kda[i][1])
            kda_lane[idx][2] += int(kda[i][2])

        for i in range(6): kda_lane[i] = round((kda_lane[i][0] + kda_lane[i][2]) / kda_lane[i][1], 2)

        ind2 = kda_lane.index(max(kda_lane[ :-1]))
        best_kda_pos = self.lane[ind2]

        if self.tier == "Unranked": tier = "Bronze"
        else: tier = self.tier

        self.lbl__pfval.setText(f"PLAY COUNT / TOTAL : {max(cnt_lane[ :-1])} / {len(position)}")
        self.lbl__pfname.setText(f"{best_cnt_pos[0]} | {best_cnt_pos[1]}")
        self.lbl__fpos.setPixmap(QPixmap(f"./ASSETS/POSITION/Position_{tier}-{best_cnt_pos[2]}.png"))

        self.lbl__pbval.setText(f"AVERAGE KDA : {max(kda_lane[ :-1])}")
        self.lbl__pbname.setText(f"{best_kda_pos[0]} | {best_kda_pos[1]}")
        self.lbl__bpos.setPixmap(QPixmap(f"./ASSETS/POSITION/Position_{tier}-{best_kda_pos[2]}.png"))

        chm_data_pos = ["top", "mid", "adc", "support", "jungle", ""]

        self.best_cnt_lane = chm_data_pos[ind1]
        self.best_kda_lane = chm_data_pos[ind2]


    def show_reco_champ(self):

        tier = ["Unranked", "Iron", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grandmaster", "Challenger"]
        tier_grade = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
        difficulty = [[0, 1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]

        n = tier.index(self.tier)
        n = tier_grade[n]
        dif = difficulty[n]

        cnt_if = self.best_cnt_chmp[5:9]
        cnt_key = self.best_cnt_chmp[1]

        cnt_champ, cnt_pick = self.pick_champ(cnt_if, cnt_key, dif)
        cnt_result = self.random_pick(cnt_pick, cnt_champ)

        kda_if = self.best_kda_chmp[5:9]
        kda_key = self.best_kda_chmp[1]

        kda_champ, kda_pick = self.pick_champ(kda_if, kda_key, dif)
        kda_result = self.random_pick(kda_pick, kda_champ)

        chm_data_pos = ["top", "mid", "adc", "support", "jungle", ""]

        cnt_pos = [""] * 2
        kda_pos = [""] * 2

        for i in range(2):

            cnt_pos[i] = self.lane[chm_data_pos.index(cnt_result[i][4])][1]
            kda_pos[i] = self.lane[chm_data_pos.index(kda_result[i][4])][1]

        self.lbl__rcham1_t.setText(cnt_result[0][1])
        self.lbl__rcham1_n.setText(cnt_result[0][2])
        self.lbl__rcham1_p.setText(f"POSITION | {cnt_pos[0]}")
        self.lbl__rcham1_d.setText(f"DIFFICULT | {int(cnt_result[0][3]):02d}")
        self.lbl__rcham1.setPixmap(QPixmap(f"./ASSETS/CHAM_LONG/{cnt_result[0][0]}.png"))

        self.lbl__rcham2_t.setText(cnt_result[1][1])
        self.lbl__rcham2_n.setText(cnt_result[1][2])
        self.lbl__rcham2_p.setText(f"POSITION | {cnt_pos[1]}")
        self.lbl__rcham2_d.setText(f"DIFFICULT | {int(cnt_result[1][3]):02d}")
        self.lbl__rcham2.setPixmap(QPixmap(f"./ASSETS/CHAM_LONG/{cnt_result[1][0]}.png"))

        self.lbl__rcham3_t.setText(kda_result[0][1])
        self.lbl__rcham3_n.setText(kda_result[0][2])
        self.lbl__rcham3_p.setText(f"POSITION | {kda_pos[0]}")
        self.lbl__rcham3_d.setText(f"DIFFICULT | {int(kda_result[0][3]):02d}")
        self.lbl__rcham3.setPixmap(QPixmap(f"./ASSETS/CHAM_LONG/{kda_result[0][0]}.png"))

        self.lbl__rcham4_t.setText(kda_result[1][1])
        self.lbl__rcham4_n.setText(kda_result[1][2])
        self.lbl__rcham4_p.setText(f"POSITION | {kda_pos[1]}")
        self.lbl__rcham4_d.setText(f"DIFFICULT | {int(kda_result[1][3]):02d}")
        self.lbl__rcham4.setPixmap(QPixmap(f"./ASSETS/CHAM_LONG/{kda_result[1][0]}.png"))

        self.lbl__link1.setText(f"<a href = \"{cnt_result[0][-1]}\">🔗</a>")
        self.lbl__link2.setText(f"<a href = \"{cnt_result[1][-1]}\">🔗</a>")
        self.lbl__link3.setText(f"<a href = \"{kda_result[0][-1]}\">🔗</a>")
        self.lbl__link4.setText(f"<a href = \"{kda_result[1][-1]}\">🔗</a>")
        

    def show_reco_lane(self):

        tier = ["Unranked", "Iron", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grandmaster", "Challenger"]
        tier_grade = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
        difficulty = [[0, 1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]

        n = tier.index(self.tier)
        n = tier_grade[n]
        dif = difficulty[n]

        cnt_lane = self.best_cnt_lane
        kda_lane = self.best_kda_lane

        cnt_champ, cnt_pick = self.pick_lane(cnt_lane, dif)
        kda_champ, kda_pick = self.pick_lane(kda_lane, dif)

        cnt_result = self.random_pick(cnt_pick, cnt_champ)
        kda_result = self.random_pick(kda_pick, kda_champ)

        chm_data_pos = ["top", "mid", "adc", "support", "jungle", ""]

        cnt_pos = self.lane[chm_data_pos.index(cnt_lane)][1]
        kda_pos = self.lane[chm_data_pos.index(kda_lane)][1]

        self.lbl__rcham5_t.setText(cnt_result[0][1])
        self.lbl__rcham5_n.setText(cnt_result[0][2])
        self.lbl__rcham5_p.setText(f"POSITION | {cnt_pos}")
        self.lbl__rcham5_d.setText(f"DIFFICULT | {int(cnt_result[0][3]):02d}")
        self.lbl__rcham5.setPixmap(QPixmap(f"./ASSETS/CHAM_LONG/{cnt_result[0][0]}.png"))

        self.lbl__rcham6_t.setText(cnt_result[1][1])
        self.lbl__rcham6_n.setText(cnt_result[1][2])
        self.lbl__rcham6_p.setText(f"POSITION | {cnt_pos}")
        self.lbl__rcham6_d.setText(f"DIFFICULT | {int(cnt_result[1][3]):02d}")
        self.lbl__rcham6.setPixmap(QPixmap(f"./ASSETS/CHAM_LONG/{cnt_result[1][0]}.png"))

        self.lbl__rcham7_t.setText(kda_result[0][1])
        self.lbl__rcham7_n.setText(kda_result[0][2])
        self.lbl__rcham7_p.setText(f"POSITION | {kda_pos}")
        self.lbl__rcham7_d.setText(f"DIFFICULT | {int(kda_result[0][3]):02d}")
        self.lbl__rcham7.setPixmap(QPixmap(f"./ASSETS/CHAM_LONG/{kda_result[0][0]}.png"))

        self.lbl__rcham8_t.setText(kda_result[1][1])
        self.lbl__rcham8_n.setText(kda_result[1][2])
        self.lbl__rcham8_p.setText(f"POSITION | {kda_pos}")
        self.lbl__rcham8_d.setText(f"DIFFICULT | {int(kda_result[1][3]):02d}")
        self.lbl__rcham8.setPixmap(QPixmap(f"./ASSETS/CHAM_LONG/{kda_result[1][0]}.png"))

        self.lbl__link8.setText(f"<a href = \"{cnt_result[0][-1]}\">🔗</a>")
        self.lbl__link6.setText(f"<a href = \"{cnt_result[1][-1]}\">🔗</a>")
        self.lbl__link5.setText(f"<a href = \"{kda_result[0][-1]}\">🔗</a>")
        self.lbl__link7.setText(f"<a href = \"{kda_result[1][-1]}\">🔗</a>")

if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = connect()
    ui.setUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
