# Windows Programming
# pyQt5
# pyside2 -> QT Designer 레이아웃 편집

import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 창을 띄우기 위한 최소 필요 모듈

class app(QWidget):

    def __init__(self):

        super().__init__()
                        # 부모 클래스의 init에 값을 부여해준다.
        self.initUI()   # 메소드 실행

    def initUI(self):
                        # 창을 띄우는 메소드
        self.setWindowTitle('Application')
                        # 창 제목 설정
        self.move(500, 500)
                        # 창 위치 조정
        self.resize(400, 200)
                        # 창 크기 조정
        self.show()     # 창 띄우기


if __name__ == '__main__':
                        # A 라는 파일 명으로 만들어 실행하면
                        # __name__은 A 가 되지만
                        # 직접 실행하면 __name__은 __main__ 이 된다.
    Qapp = QApplication(sys.argv)
                        # 모든 PyQt5 어플리케이션은 객체로 생성해야한다.
    e = app()
    sys.exit(Qapp.exec_())
                        # Qapp 객체를 실행
                        # system의 x 를 누르면 app 종료
