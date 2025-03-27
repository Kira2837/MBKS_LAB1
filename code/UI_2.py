from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 706)
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 77);")
        MainWindow.setWindowIcon(QtGui.QIcon(r'..\picture\iconhacker.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 150, 41, 31))
        self.label_2.setStyleSheet("border-image: url(:/pic/picture/click_png.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Attack = QtWidgets.QPushButton(self.centralwidget)
        self.Attack.setGeometry(QtCore.QRect(620, 140, 101, 51))
        self.Attack.setStyleSheet("border-image: url(:/pic/picture/red_btn.png);\n"
"font: 12pt \"MV Boli\";")
        self.Attack.setObjectName("Attack")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 450, 231, 51))
        self.label_3.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/blu.jpg);")
        self.label_3.setObjectName("label_3")
        self.Read = QtWidgets.QPushButton(self.centralwidget)
        self.Read.setGeometry(QtCore.QRect(620, 450, 101, 51))
        self.Read.setStyleSheet("border-image: url(:/pic/picture/red_btn.png);\n"
"font: 12pt \"MV Boli\";")
        self.Read.setObjectName("Read")
        self.Path = QtWidgets.QPushButton(self.centralwidget)
        self.Path.setGeometry(QtCore.QRect(480, 450, 131, 51))
        self.Path.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/ylw_btn.png);")
        self.Path.setObjectName("Path")
        self.File = QtWidgets.QLabel(self.centralwidget)
        self.File.setGeometry(QtCore.QRect(290, 450, 171, 51))
        self.File.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/white.jpg);")
        self.File.setText("")
        self.File.setObjectName("File")
        self.Finish = QtWidgets.QPushButton(self.centralwidget)
        self.Finish.setGeometry(QtCore.QRect(620, 320, 101, 51))
        self.Finish.setStyleSheet("border-image: url(:/pic/picture/red_btn.png);\n"
"font: 12pt \"MV Boli\";")
        self.Finish.setObjectName("Finish")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 330, 41, 31))
        self.label_4.setStyleSheet("border-image: url(:/pic/picture/click_png.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.ListFile = QtWidgets.QListWidget(self.centralwidget)
        self.ListFile.setGeometry(QtCore.QRect(40, 70, 461, 181))
        self.ListFile.setStyleSheet("font: 12pt \"MV Boli\";\n"
"color: rgb(0, 255, 0);")
        self.ListFile.setObjectName("ListFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 181, 21))
        self.label.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/blu.jpg);")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 260, 261, 21))
        self.label_5.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/blu.jpg);")
        self.label_5.setObjectName("label_5")
        self.Status = QtWidgets.QListWidget(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(40, 290, 461, 131))
        self.Status.setStyleSheet("font: 12pt \"MV Boli\";\n"
"color: rgb(0, 255, 0);")
        self.Status.setObjectName("Status")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 530, 221, 61))
        self.label_6.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/blu.jpg);")
        self.label_6.setObjectName("label_6")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(290, 530, 291, 121))
        self.info.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/white.jpg);")
        self.info.setText("")
        self.info.setObjectName("info")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(620, 560, 111, 51))
        self.Reset.setStyleSheet("border-image: url(:/pic/picture/red_btn.png);\n"
"font: 12pt \"MV Boli\";")
        self.Reset.setObjectName("Reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attack app"))
        self.Attack.setText(_translate("MainWindow", "Attack"))
        self.label_3.setText(_translate("MainWindow", "Enter the file name to copy\n"
" and to read:"))
        self.Read.setText(_translate("MainWindow", "Read"))
        self.Path.setText(_translate("MainWindow", "Select path"))
        self.Finish.setText(_translate("MainWindow", "Finish"))
        self.label.setText(_translate("MainWindow", "The folder scaned:"))
        self.label_5.setText(_translate("MainWindow", "Status of folders and files:"))
        self.label_6.setText(_translate("MainWindow", "Information contained\n"
" in the file:"))
        self.Reset.setText(_translate("MainWindow", "Reset app"))
import Resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
