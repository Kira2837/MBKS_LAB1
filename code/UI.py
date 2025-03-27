from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 608)
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 77);")
        MainWindow.setWindowIcon(QtGui.QIcon(r'.\picture\iconuser.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 121, 31))
        self.label.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/blu.jpg);")
        self.label.setObjectName("label")
        self.Text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(30, 90, 491, 311))
        self.Text.setStyleSheet("font: 12pt \"MV Boli\";\n"
"color: rgb(0, 255, 0);")
        self.Text.setObjectName("Text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 41, 31))
        self.label_2.setStyleSheet("border-image: url(:/pic/picture/click_png.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(600, 200, 101, 51))
        self.Save.setStyleSheet("border-image: url(:/pic/picture/red_btn.png);\n"
"font: 12pt \"MV Boli\";")
        self.Save.setObjectName("Save")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 470, 231, 51))
        self.label_3.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/blu.jpg);")
        self.label_3.setObjectName("label_3")
        self.Copy = QtWidgets.QPushButton(self.centralwidget)
        self.Copy.setGeometry(QtCore.QRect(600, 470, 101, 51))
        self.Copy.setStyleSheet("border-image: url(:/pic/picture/red_btn.png);\n"
"font: 12pt \"MV Boli\";")
        self.Copy.setObjectName("Copy")
        self.Path = QtWidgets.QPushButton(self.centralwidget)
        self.Path.setGeometry(QtCore.QRect(460, 470, 131, 51))
        self.Path.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/ylw_btn.png);")
        self.Path.setObjectName("Path")
        self.File = QtWidgets.QLabel(self.centralwidget)
        self.File.setGeometry(QtCore.QRect(270, 470, 171, 51))
        self.File.setStyleSheet("font: 12pt \"MV Boli\";\n"
"border-image: url(:/pic/picture/white.jpg);")
        self.File.setText("")
        self.File.setObjectName("File")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User app"))
        self.label.setText(_translate("MainWindow", "Enter text:"))
        self.Save.setText(_translate("MainWindow", "Save As"))
        self.label_3.setText(_translate("MainWindow", "Enter the file name to copy\n"
" to the public folder:"))
        self.Copy.setText(_translate("MainWindow", "Copy"))
        self.Path.setText(_translate("MainWindow", "Select path"))
import Resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
