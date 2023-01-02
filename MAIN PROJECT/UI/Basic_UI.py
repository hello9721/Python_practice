import sys
import sqlite3 as sql
import numpy as np
import pandas as pd

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import matplotlib.pyplot as pl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import tensorflow as tf
import tensorflow.keras as keras
from sklearn.preprocessing import MinMaxScaler as MMS

from Calendar_Widget import *

class Apps(QWidget):

    def __init__(self) :
        
        super().__init__()
        self.initUI()
        
    def initUI(self) :                                      # 윈도우 환경 구성

        ## 레이아웃

        layout_main = QVBoxLayout()

        layout_one = QVBoxLayout()                          # 조회, 검색
        layout_two = QHBoxLayout()                          # 전체 요약
        layout_thr = QHBoxLayout()                          # 12월 예측

        layout_search = QHBoxLayout()                       # one - 검색 ( 라인에딧, 버튼, 결과라벨 )
        layout_select = QHBoxLayout()                       # one - 조회 ( 콤보상자, 버튼, 라디오버튼1, 2 )

        layout_main.addLayout(layout_one)                   # 메인 레이아웃에 세부 레이아웃 추가
        layout_main.addLayout(layout_two)
        layout_main.addLayout(layout_thr)

        layout_one.addLayout(layout_search)                 # 첫번째 레이아웃에 세부 레이아웃 추가
        layout_one.addLayout(layout_select)

        ## layout_one > layout_search

        self.ln_search = QLineEdit("")                      # 검색 값 입력창
        self.btn_search = QPushButton("SEARCH")             # 검색 함수 실행 버튼
        self.lbl_result = QLabel("검색결과 : -")            # 검색 결과 표시 라벨 ( 검색완료 혹은 검색결과 없음 )

        self.ln_search.setStyleSheet("height: 20px;")       # 검색 위젯들 높이 설정
        self.btn_search.setStyleSheet("height: 20px;")
        self.lbl_result.setStyleSheet("height: 20px;")

        layout_search.addWidget(self.ln_search, 3)          # 검색 레이아웃에 위젯 추가
        layout_search.addWidget(self.btn_search, 1)
        layout_search.addWidget(self.lbl_result, 1)

        ## layout_one > layout_select

        self.cmb_select = QComboBox(self)                   # 장비 선택 콤보상자
        self.btn_select = QPushButton("SELECT")             # 선택 후 조회 버튼
        
        self.rdo_search = QRadioButton("SEARCH")            # 검색모드 활성화
        self.rdo_select = QRadioButton("SELECT")            # 조회모드 활성화

        self.rdo_search.setChecked(True)                    # 체크 활성화

        self.cmb_select.setStyleSheet("height: 20px;")      # 조회 위젯들 높이 설정
        self.btn_select.setStyleSheet("height: 20px;")
        self.rdo_search.setStyleSheet("height: 20px;")
        self.rdo_select.setStyleSheet("height: 20px;")

        layout_select.addWidget(self.cmb_select, 6)         # 조회 레이아웃에 위젯 추가
        layout_select.addWidget(self.btn_select, 2)
        layout_select.addWidget(self.rdo_search, 1)
        layout_select.addWidget(self.rdo_select, 1)

        ## layout_two

        self.fig_two = pl.Figure(figsize = (5, 3))          # 전체 그래프 canvas 설정
        self.canv_two = FigureCanvas(self.fig_two)        

        self.txt_two = QTextEdit("")                        # 전체 요약 텍스트

        layout_two.addWidget(self.canv_two, 1)              # 두번째 레이아웃에 위젯추가
        layout_two.addWidget(self.txt_two, 1)                  

        ## layout_thr

        self.fig_thr = pl.Figure(figsize = (5, 3))          # 12월 예측 그래프 canvas 설정
        self.canv_thr = FigureCanvas(self.fig_thr)        

        self.cln_thr = Calendar(self)                       # 달력 위젯
        self.cln_thr.setCursor(Qt.PointingHandCursor)

        layout_thr.addWidget(self.canv_thr, 1)              # 세번째 레이아웃에 위젯추가
        layout_thr.addWidget(self.cln_thr, 1)

        ## 윈도우 설정

        self.setLayout(layout_main)
        self.setWindowTitle('Pred Temp Viewer')
        self.setGeometry(0, 30, 1100, 900)
        self.show()



if __name__ == '__main__' :
    
    app = QApplication(sys.argv)
    ex = Apps()
    sys.exit(app.exec_())