# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P_20_1_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):

    encode = "utf-8"
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.txt__hex = QtWidgets.QTextEdit(self.centralwidget)
        self.txt__hex.setGeometry(QtCore.QRect(10, 10, 383, 740))
        self.txt__hex.setObjectName("txt__hex")
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(12)
        self.txt__hex.setFont(font)

        self.txt__txt = QtWidgets.QTextEdit(self.centralwidget)
        self.txt__txt.setGeometry(QtCore.QRect(407, 10, 383, 740))
        self.txt__txt.setObjectName("txt__txt")
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(12)
        self.txt__txt.setFont(font)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.m__bar = QtWidgets.QMenuBar(MainWindow)
        self.m__bar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.m__bar.setObjectName("m__bar")
        
        self.m__file = QtWidgets.QMenu(self.m__bar)
        self.m__file.setObjectName("m__file")
        
        self.m__option = QtWidgets.QMenu(self.m__bar)
        self.m__option.setObjectName("m__option")
        MainWindow.setMenuBar(self.m__bar)
        
        self.s__bar = QtWidgets.QStatusBar(MainWindow)
        self.s__bar.setObjectName("s__bar")
        MainWindow.setStatusBar(self.s__bar)
        
        self.act__open = QtWidgets.QAction(MainWindow)
        self.act__open.setObjectName("act__open")
        
        self.act__save = QtWidgets.QAction(MainWindow)
        self.act__save.setObjectName("act__save")
        
        self.act__reset = QtWidgets.QAction(MainWindow)
        self.act__reset.setObjectName("act__reset")
        
        self.act__utf = QtWidgets.QAction(MainWindow)
        self.act__utf.setCheckable(True)
        self.act__utf.setChecked(True)
        self.act__utf.setObjectName("act__utf")
        
        self.act__ansi = QtWidgets.QAction(MainWindow)
        self.act__ansi.setCheckable(True)
        self.act__ansi.setObjectName("act__ansi")
        
        self.m__file.addAction(self.act__open)
        self.m__file.addAction(self.act__save)
        self.m__file.addAction(self.act__reset)
        
        self.m__option.addAction(self.act__utf)
        self.m__option.addAction(self.act__ansi)
        
        self.m__bar.addAction(self.m__file.menuAction())
        self.m__bar.addAction(self.m__option.menuAction())

        self.act__utf.triggered.connect(self.encoding_utf)
        self.act__ansi.triggered.connect(self.encoding_ansi)

        self.act__open.triggered.connect(self.open)
        self.act__save.triggered.connect(self.save)
        self.act__reset.triggered.connect(self.reset)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def encoding_utf(self):

        self.encode = "utf-8"
        self.act__utf.setChecked(True)
        self.act__ansi.setChecked(False)

        self.s__bar.showMessage("Now Encoding Type => UTF-8")
        
    def encoding_ansi(self):

        self.encode = "cp949"
        self.act__utf.setChecked(False)
        self.act__ansi.setChecked(True)

        self.s__bar.showMessage("Now Encoding Type => ANSI")

    def path_selector(self):

        path = QtWidgets.QFileDialog.getOpenFileName(self, "Select File...")

        return path[0]

    def open(self):

        cnt = 0

        path = self.path_selector()
        
        temp1 = ""
        temp2 = ""
                
        f = open(path, "r", encoding = self.encode)

        for i in f:

            i = i.split("\n")[0]
            
            for j in bytes(i, self.encode):

                temp1 += hex(j).split("x")[1]
                temp2 += chr(j)
                
                cnt += 1

                if cnt == 8:

                    temp1 += "\n"
                    temp2 += "\n"
                    
                    cnt = 0
                    
                else:

                    temp1 += "  "
                    temp2 += "  "

        f.close()

        self.txt__hex.setText(temp1)
        self.txt__txt.setText(temp2)

    def save(self):

        path = self.path_selector()

        temp = self.txt__hex.toPlainText()

        f = open(path, "w", encoding = self.encode)

        f.write(temp)

        f.close()
        
        
    def reset(self):

        self.txt__hex.setText("")
        self.txt__txt.setText("")

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEXT -> HEX EDITER"))
        self.m__file.setTitle(_translate("MainWindow", "File"))
        self.m__option.setTitle(_translate("MainWindow", "Option"))
        self.act__open.setText(_translate("MainWindow", "Open"))
        self.act__save.setText(_translate("MainWindow", "Save"))
        self.act__reset.setText(_translate("MainWindow", "Reset"))
        self.act__utf.setText(_translate("MainWindow", "UTF-8"))
        self.act__ansi.setText(_translate("MainWindow", "ANSI"))


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
