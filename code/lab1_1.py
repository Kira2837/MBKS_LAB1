from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from UI import Ui_MainWindow
import shutil
import os

class MAIN_HANDLE(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(MainWindow)
        self.Copy.setEnabled(False)

        self.PublicDir = r"..\public"
        self.PrivateDir = r"..\private"

        self.Save.clicked.connect(self.SaveFile)
        self.Path.clicked.connect(self.SelectFiletoCopy)
        self.Copy.clicked.connect(self.CopyFileToPublicFolder)
        
    def GetData(self):
        text = str(self.Text.toPlainText())
        return text

    def SaveFile(self):
        widget = self.centralwidget
        filename, _ = QFileDialog.getSaveFileName(widget, "Save file", self.PrivateDir, "Text files (*.txt)")

        if filename:
            with open(filename, "w") as f:
                text = self.GetData()
                f.write(text)
        self.Text.setPlainText('')

    def SelectFiletoCopy(self):
        widget = self.centralwidget
        source_file, _ = QFileDialog.getOpenFileName(widget, "Choose source file", self.PrivateDir, "All Files (*)")
        self.File.setText(source_file)
        self.File.setWordWrap(True)
        self.Copy.setEnabled(True)

    def CopyFileToPublicFolder(self):
        source_file = self.File.text()
        if source_file and self.PublicDir:
            try:
                shutil.copyfile(source_file, os.path.join(self.PublicDir, os.path.basename(source_file)))
                self.ShowStatus("Success!", "Copy file successfully!!!", True)
            except:
                self.ShowStatus("Error!", "Copying files failed", False)

    def ShowStatus(self, Title, Message, Status):
        error = QMessageBox()
        error.setWindowTitle(Title)
        error.setText(Message)
        if not Status:
            error.setIcon(QMessageBox.Critical) 
        else:
            error.setIcon(QMessageBox.Information) 
        error.setStandardButtons(QMessageBox.Ok) 
        error.setDefaultButton(QMessageBox.Ok) 
        error.setStyleSheet("font: 14pt \"MV Boli\";\n""color: rgb(255, 0, 0);")
        error.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MAIN_HANDLE()
    MainWindow.show()
    sys.exit(app.exec_())