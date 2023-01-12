from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Calendar(QCalendarWidget):
  
    def paintCell(self, painter, rect, date):

        print(super(Calendar, self))

        super(Calendar, self).paintCell(painter, rect, date)

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

            painter.drawText(                                                   # 셀 객체의 center - (14, -20) 위치에 해당 포맷으로 문자 그리기
                rect.center() - QPoint(14, -20),
                "{}".format("5235"),
            )

            painter.restore()                                                   # 그리기 종료
