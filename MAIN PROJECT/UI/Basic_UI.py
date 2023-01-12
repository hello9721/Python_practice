import sys
import sqlite3 as sql
import numpy as np
import pandas as pd

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import matplotlib.pyplot as pl
from matplotlib import font_manager, rc
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler as MMS

from Calendar_Widget import *

class Apps(QWidget):

    def __init__(self) :
        
        super().__init__()
        self.initUI()
        
    def initUI(self) :                                      # 윈도우 환경 구성

        self.select_mode = False                            # 모드 종류 구별 용도

        self.conn = sql.connect('Power_Data.db')
        
        ## 레이아웃

        self.layout_main = QVBoxLayout()

        self.layout_one = QVBoxLayout()                          # 조회, 검색
        self.layout_two = QHBoxLayout()                          # 전체 요약
        self.layout_thr = QHBoxLayout()                          # 12월 예측

        self.layout_search = QHBoxLayout()                       # one - 검색 ( 라인에딧, 버튼, 결과라벨 )
        self.layout_select = QHBoxLayout()                       # one - 조회 ( 콤보상자, 버튼, 라디오버튼1, 2 )

        self.layout_main.addLayout(self.layout_one)                   # 메인 레이아웃에 세부 레이아웃 추가
        self.layout_main.addLayout(self.layout_two)
        self.layout_main.addLayout(self.layout_thr)

        self.layout_one.addLayout(self.layout_search)                 # 첫번째 레이아웃에 세부 레이아웃 추가
        self.layout_one.addLayout(self.layout_select)

        ## self.layout_one > self.layout_search

        self.ln_search = QLineEdit("")                      # 검색 값 입력창
        self.btn_search = QPushButton("SEARCH")             # 검색 함수 실행 버튼
        self.btn_search.clicked.connect(self.btn_Select)
        self.lbl_result = QLabel("검색결과 : -")            # 검색 결과 표시 라벨 ( 검색완료 혹은 검색결과 없음 )
                                                            # 위젯 크기설정
        self.ln_search.setStyleSheet("height: 25px;")
        self.btn_search.setStyleSheet("height: 25px;")
        self.lbl_result.setStyleSheet("height: 25px;")

        self.layout_search.addWidget(self.ln_search, 6)          # 검색 레이아웃에 위젯 추가
        self.layout_search.addWidget(self.btn_search, 2)
        self.layout_search.addWidget(self.lbl_result, 2)

        ## self.layout_one > self.layout_select

        self.cmb_select = QComboBox(self)                   # 장비 선택 콤보상자

        self.lis = self.Combolis()                          # 콤보상자 리스트 목록
        self.cmb_select.addItems(self.lis) 

        self.cmb_select.setEditable(True)                   # 가운데 정렬을 위해 Editable로 설정 후
        self.cmb_select.lineEdit().setReadOnly(True)        # ReadOnly를 설정하여 수정 방지
        self.cmb_select.lineEdit().setAlignment(Qt.AlignCenter)
                                                            # 가운데 설정

        for i in range(self.cmb_select.count()): self.cmb_select.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)
                                                            # 콤보박스 안의 텍스트 가운데 정렬

        cmb_view = QListView()                              # 콤보 박스 안의 높이 조절을 위해 ListView 생성
        cmb_view.setStyleSheet("QListView::item{"           # 스타일시트로 높이 설정
                                    "height: 25px;"
                                    "}")

        self.cmb_select.setView(cmb_view)                   # ListView 객체를 콤보박스에 적용

        self.btn_select = QPushButton("SELECT")             # 선택 후 조회 버튼
        self.btn_select.clicked.connect(self.btn_Select)
        
        self.rdo_search = QRadioButton("SEARCH")            # 검색모드 활성화
        self.rdo_select = QRadioButton("SELECT")            # 조회모드 활성화

        self.rdo_search.setChecked(True)                    # 체크 활성화
                                                            # 위젯 크기설정
        self.cmb_select.setStyleSheet("height: 25px;")
        self.btn_select.setStyleSheet("height: 25px;")
        self.rdo_search.setStyleSheet("height: 25px;")
        self.rdo_select.setStyleSheet("height: 25px;")

        self.layout_select.addWidget(self.cmb_select, 6)         # 조회 레이아웃에 위젯 추가
        self.layout_select.addWidget(self.btn_select, 2)
        self.layout_select.addWidget(self.rdo_search, 1)
        self.layout_select.addWidget(self.rdo_select, 1)

        ## self.layout_two

        self.fig_two = pl.Figure(figsize = (5, 3))          # 전체 그래프 canvas 설정
        self.canv_two = FigureCanvas(self.fig_two)        

        self.ncol = 1
        self.tbl_two = QTableWidget(12, self.ncol)          # 테이블 설정
        self.tbl_two.setVerticalHeaderLabels(['01월', '02월', '03월', '04월', '05월', '06월', '07월', '08월', '09월', '10월', '11월', '총'])
                                                            # 행 이름 설정
        self.tbl_two.setHorizontalHeaderLabels(['한달 사용량'])

        self.layout_two.addWidget(self.canv_two, 1)              # 두번째 레이아웃에 위젯추가
        self.layout_two.addWidget(self.tbl_two, 1)

        tbl_width = int(self.tbl_two.width()/self.tbl_two.columnCount()*0.75)
                                                            # 테이블 셀 너비 자동 조정
        for i in range(self.tbl_two.columnCount()): self.tbl_two.setColumnWidth(i, tbl_width)

        ## self.layout_thr

        self.fig_thr = pl.Figure(figsize = (5, 3))          # 12월 예측 그래프 canvas 설정
        self.canv_thr = FigureCanvas(self.fig_thr)        

        self.cln_thr = Calendar(self)                       # 달력 위젯
        self.cln_thr.setCursor(Qt.PointingHandCursor)

        self.layout_thr.addWidget(self.canv_thr, 1)              # 세번째 레이아웃에 위젯추가
        self.layout_thr.addWidget(self.cln_thr, 1)

        ## 그래프 실험용 df

        # self.df = pd.DataFrame(data = [1, 2, 3, 1, 4, 5, 6, 8, 9])
        # self.graph_two()

        ## 윈도우 설정

        self.setLayout(self.layout_main)
        self.setWindowTitle('Pred Temp Viewer')
        self.setGeometry(0, 30, 1100, 900)
        self.show()
        
        self.btn_select.setEnabled(False)                  # 초기 조회 모드 비활성화
        self.cmb_select.setEnabled(False)

        self.rdo_search.clicked.connect(self.rdo_searchbtn) # 모드에 따른 기능 비활성화
        self.rdo_select.clicked.connect(self.rdo_selectbtn)

    def rdo_searchbtn (self) :                              # 검색 모드

        if self.rdo_search.isCheckable() == True :
            
            self.btn_search.setEnabled(True)
            self.btn_select.setEnabled(False)
            self.ln_search.setEnabled(True)
            self.cmb_select.setEnabled(False)

            self.select_mode = False

    def rdo_selectbtn (self) :                              # 조회모드
        
        if self.rdo_select.isCheckable() == True :

            self.btn_search.setEnabled(False)
            self.btn_select.setEnabled(True)
            self.ln_search.setEnabled(False)
            self.cmb_select.setEnabled(True)

            self.select_mode = True

    def Combolis (self) :                                   # 콤보상자 리스트

        f = open("CODE.csv")
        lis = f.read().split('\n')[0].split(',')
        f.close()
        
        return lis

    def graph_two(self):                                    # 그래프 그리기

        self.df_pre = pd.DataFrame(self.result, columns = ['id', 'power_value', 'updated'])                 # self.result 를 데이터프레임으로 만들기
        self.df_pre['updated'] = pd.to_datetime(self.df_pre.updated, format = '%Y-%m-%d %H:%M')             # updated 날짜 문자형 -> 날짜형으로 변환

        self.df_drop = self.df_pre.drop(['id'], axis = 1)                                                   # 장비 id 열 제거

        x = self.df_drop['updated']                                                                         # x 축 날짜로 만들기 위한 변수 설정
        y = self.df_drop['power_value']                                                                     # y 축 값으로 만들기 위한 변수 설정

        # self.df로 데이터프레임화된 데이터 저장하기
        # 아래 그래프에 사용하는 데이터 수정하기

        self.fig_two.clear()
        
        graph_font = font_manager.FontProperties(fname = "c:/Windows/Fonts/malgun.ttf", weight = 'bold')    # windows 용 글꼴
        
        ax = self.fig_two.add_subplot(111)
        ax.clear()
        
        ax.plot(x, y)
        
        ax.set_title(f'계량기 {self.device_id} 번의 관측 값', fontsize = 15, fontproperties = graph_font)

        ax.tick_params(axis = 'both', labelsize = 6.5)
        self.cursor.close()
        
        self.canv_two.draw()
        
    def graph_thr(self):

        self.fig_thr.clear()
        
        graph_font = font_manager.FontProperties(fname = "c:/Windows/Fonts/malgun.ttf", weight = 'bold')    # windows 용 글꼴
        
        ax = self.fig_thr.add_subplot(111)
        ax.clear()
        
        ax.plot(self.pred_data)
        
        ax.set_title(f'계량기 {self.device_id} 번의 12월 예측 값', fontsize = 15, fontproperties = graph_font)

        ax.tick_params(axis = 'both', labelsize = 6.5)
        
        self.canv_thr.draw()

    def table_setting(self):                                # 표 데이터 넣기
                                                            # 한달 사용량을 리스트로 만드는 부분 추가하기 + 총 사용량

        self.cursor = self.conn.cursor()

        value_list = []

        for i in range(1, 12) :

            query = f"select power_value from [{self.device_id}] where strftime('%m',updated)='{i:02d}'"
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            val = result[-1][0] - result[0][0]
            value_list.append(val)

        for i in range(11):

            for j in range(self.ncol):

                item = QTableWidgetItem(f'{value_list[i]:.2f}')
                item.setTextAlignment(Qt.AlignCenter)
                
                self.tbl_two.setItem(i, j, item)

        item = QTableWidgetItem(f'{sum(value_list):.2f}')
        item.setTextAlignment(Qt.AlignCenter)

        self.tbl_two.setItem(11, 0, item)

    def getDataSetX(self, item, start, to, size) :

        arr = []

        for i in range(start, to - (size-1)) :

            arr.append(item[i:i+size , 0])
        
        nparr = np.array(arr)
        nparr = np.reshape(nparr, (nparr.shape[0], nparr.shape[1], 1))

        return (nparr)

    def model_pred(self):
        
        query = f'select * from "{self.device_id}" where date(updated) >= "2022-11-24" and date(updated) <= "2022-11-30"'
        self.cursor.execute(query)

        data = self.cursor.fetchall()
        data = [i[1] for i in data]
        
        model = tf.keras.models.load_model(f'MODEL\lstm_model_{self.device_id}.h5')
        scaler_tool = MMS(feature_range = (0, 1))

        for i in range(31):

            a = 0 + i
            b = 6 + i
            
            in_data = pd.DataFrame(data)
            in_data = in_data.values

            scaled_data = scaler_tool.fit_transform(in_data)
            dataset = self.getDataSetX(scaled_data, a, b+1, 7)
            
            pred = model.predict(dataset)
            pred = scaler_tool.inverse_transform(pred)
            pred = pred[0].tolist()
            pred = round(pred[0], 1)
            
            data.append(pred)

        self.pred_data = data[7: ]

    def pred_reset(self):

        f = open("./PRED_DATA.csv", 'w')
        f.close()

    def pred_save(self):

        f = open("./PRED_DATA.csv", 'w')
        cnt = 0

        for i in self.pred_data:
            
            if cnt == 0: 
                
                f.write(f"{i}")
                cnt += 1

            else: f.write(f", {i}")

        f.close()


    def btn_Select(self) :

        if self.select_mode: self.device_id = self.cmb_select.currentText().strip()
                                                                # 콤보박스로 설정된 텍스트 가져오기
        else: self.device_id = self.ln_search.text()            # 라인에딧 텍스트 가져오기

        # try:

        self.cursor = self.conn.cursor()                        
        query = 'select * from [%s]' % (self.device_id)         # 숫자로 이루어진 테이블 값 쿼리로 가져오기 [] 활용

        self.cursor.execute(query)
        self.result = self.cursor.fetchall()

        self.graph_two()
        self.table_setting()
        self.model_pred()
        self.pred_save()
        self.graph_thr()
        self.new_cln = Calendar(self)
        self.new_cln.setCursor(Qt.PointingHandCursor)

        self.layout_thr.insertWidget(1, self.new_cln, 1)
        self.layout_thr.removeWidget(self.cln_thr)

        self.cln_thr = self.new_cln

        self.lbl_result.setText(f"검색결과 : {len(self.result)} 일의 데이터 검색 완료.")

        # except: self.lbl_result.setText("검색결과 : 다시 입력 요망.")

if __name__ == '__main__' :
    
    app = QApplication(sys.argv)
    ex = Apps()
    sys.exit(app.exec_())