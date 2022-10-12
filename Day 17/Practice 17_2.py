import sys
from PyQt5 import QtWidgets, uic
# Widgets -> 버튼, 콤보박스 등등 각종 기능들

class form(QtWidgets.QDialog):
                                # 클래스 form은 QDialog를 상속 받음
    fname = ""                  # 폼의 이름
    fm = ""                     # 이름을 통해 가지고 온 폼
        
    def __init__(self, name):   # 생성자
        
        self.fname = name       # loadUi에 fname을 넣어 폼을 반환 받음
        self.fm = uic.loadUi(self.fname)
        self.fm.show()          # 폼 띄우기

app = QtWidgets.QApplication(sys.argv)

f = form("./repo/Practice_17_2.ui")
                                # form의 객체화
sys.exit(app.exec_())           # x 를 누르면 실행 종료


#---------------------------------------------------------------------------#

# cmd 명령어를 bat 파일로 만들어서 사용

# python -m PyQt5.uic.pyuic -x %1 -o %2
# 라는 내용의 bat 파일을 생성

# cmd 에서 해당 파일들이 있는 폴더로 디렉토리를 이동해서

# bat이름.bat %1.ui %2.py

# 를 입력하면 띄어쓰기로 구분되어 0번째 요소가 실행되어
# %1 자리에 1번째 요소가 들어가고 %2 자리에 2번째 요소가 들어간다.

# 위의 명령어 같은 경우 pyuic를 이용하여 ui 파일을 py 파일로 변환해준다.
# %1 이 input 이 되고 %2 이 output 이 되는 것이다.

# (+) 파일 이름에는 띄어쓰기가 없어야한다.

#---------------------------------------------------------------------------#

# cmd path 추가
# Path = Path;경로\
