# text edit 를 사용하여 버튼을 추가로 만들고
# text value를 대문자 혹은 소문자로 만들어주는 창 만들기

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P_18_1_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 50, 740, 90))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setLineWidth(0)
        self.textEdit.setObjectName("textEdit")
        self.btn__lower = QtWidgets.QPushButton(self.centralwidget)
        self.btn__lower.setGeometry(QtCore.QRect(30, 150, 230, 50))
        self.btn__lower.setObjectName("btn__lower")
        self.btn__reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn__reset.setGeometry(QtCore.QRect(540, 150, 230, 50))
        self.btn__reset.setObjectName("btn__reset")
        self.btn__upper = QtWidgets.QPushButton(self.centralwidget)
        self.btn__upper.setGeometry(QtCore.QRect(286, 150, 230, 50))
        self.btn__upper.setObjectName("btn__upper")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(26, 190, 741, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label.setEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn__lower.clicked.connect(self.toLower)
        self.btn__upper.clicked.connect(self.toUpper)
        self.btn__reset.clicked.connect(self.reset)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def toLower(self):

        temp = self.textEdit.toPlainText()

        self.textEdit.setText(temp.lower())

    def toUpper(self):

        temp = self.textEdit.toPlainText()

        self.textEdit.setText(temp.upper())

    def reset(self):

        self.textEdit.setText("")

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lower - Upper Converter"))
        self.btn__lower.setText(_translate("MainWindow", "To Lower"))
        self.btn__reset.setText(_translate("MainWindow", "Reset"))
        self.btn__upper.setText(_translate("MainWindow", "To Upper"))
        self.label.setText(_translate("MainWindow", "Lower - Upper Converter"))


if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
