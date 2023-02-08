from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Calendar(QCalendarWidget):
  
    def paintCell(self, painter, rect, date):

        super(Calendar, self).paintCell(painter, rect, date)

        f = open("./DATA/PRED_DATA.csv")                                             # 예측값 파일 불러오기

        data = f.read()
        if data != "":                                                          # 첫 실행이 아니라서 비어있지 않다면

            data = data.split(",")                                              # , 를 구분자로 분리 후 공백 제거하고 float로 변환
            data = [float(i.strip()) for i in data]

        self.setMinimumDate(QDate(2022, 12, 1))                                 # 달력 표시 범위 설정
        self.setMaximumDate(QDate(2022, 12, 31))

        self.setStyleSheet("selection-background-color: rgb(230, 230, 230);"    # 선택 셀 색 설정
                           "selection-color: #000;")
        self.setVerticalHeaderFormat(0)                                         # 0 = 행번호 제거
        self.setGridVisible(True)

        if (date >= QDate(2022, 12, 1)) & (date <= QDate(2022, 12, 31)):        # 글씨 12월에만 표시

            painter.save()                                                      # 그리기 시작

            painter.setPen(QColor(150, 150, 150))                               # 글씨 색 설정
            if date == self.selectedDate(): painter.setPen(QColor(100, 100, 100))
                                                                                # 선택된 셀이라면 좀더 진하게

            font = QFont()                                                      # 그릴 텍스트의 폰트 모양 설정
            font.setPixelSize(11)
            font.setBold(True)
            # font.setItalic(True)
            
            painter.setFont(font)                                               # 페인터에 폰트 적용
            
            if data != "": txt = f"{data[date.day() - 1]}"                      # 비어있지 않다면 현재 Cell (date) 의 day (int형) -1 인덱스에 있는 값 저장
            else: txt = ""                                                      # 첫 실행이라 파일이 초기화된 상태라서 data가 비어있다면 빈 문자열 저장

            painter.drawText(                                                   # 셀 객체의 center - (14, -20) 위치에
            rect.center() - QPoint(18, -20),
            txt,                                                                # 저장된 문자열 그리기
            )

            painter.restore()                                                   # 그리기 종료
