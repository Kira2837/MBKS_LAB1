from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QFileSystemWatcher, QDir
from PyQt5.QtGui import QColor
from UI_2 import Ui_MainWindow
import shutil
import os
from datetime import datetime
import hashlib

class MAIN_HANDLE(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(MainWindow)

        self.PublicDir = r".\public"
        self.AttackDir = r".\attack"

        self.Dir = QDir(self.PublicDir)
        self.Dir_1 = QDir(self.AttackDir)
        self.watcher = QFileSystemWatcher()
        self.SetDefaultApp()
        self.files_and_contents = []

        self.Attack.clicked.connect(lambda: self.Watcher(self.PublicDir))
        self.Finish.clicked.connect(self.FinishWatcher)
        self.Path.clicked.connect(self.SelectFiletoRead)
        self.Read.clicked.connect(self.ReadFileToClipBoard)
        self.Reset.clicked.connect(self.ResetApp)   
    
    def listFile(self, directory):
        path_files = []
        title = f'''List of files in folder {directory} (highlighted 
in red are deleted files):'''
        self.ListFile.addItem(title)
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                path_files.append(path.replace("\\", "/"))
                self.ListFile.addItem(filename)
        return path_files
        
    def on_file_changed(self, path):
        self.Dir.refresh()
        filename = os.path.basename(path)
        if os.path.exists(path):
            content_index = self.GetContentFile(filename)
            index = content_index[1]
            OldContent = content_index[0]
            NewContent = self.ContentFileToSha256(path)
            if os.path.isfile(path) and NewContent != OldContent:
                self.files_and_contents[index][1] = NewContent
                message = f"File {path}\n has been modified."
                self.Status.addItem(message)
                try:
                    file_time = datetime.now().strftime("%d-%m-%y_%H-%M-%S-%f")
                    file_copied = os.path.join(self.AttackDir, os.path.basename(path)).replace(".txt", f"_{file_time}.txt")
                    
                    shutil.copyfile(path, file_copied)
                except:
                    self.ShowStatus("Error!", "Copying files failed", False)
        else:
            message = f"File {path} deleted!"
            self.Status.addItem(message)
            self.watcher.removePath(path)
            for i in range(len(self.files_and_contents)):
                if self.files_and_contents[i][0] == filename:
                    self.files_and_contents.remove(self.files_and_contents[i])
                    break
            items = self.ListFile.findItems(filename, QtCore.Qt.MatchExactly)
            for item in items:
                color = QColor(255, 0, 0)
                item.setForeground(color)

    def on_directory_changed(self):
        self.Dir.refresh()
        self.label_5.show() 
        self.Status.show()
        files = self.Dir.entryList()
        files.remove('.')
        files.remove('..')
        current_files = []
        for i in range(len(self.files_and_contents)):
            current_files.append(self.files_and_contents[i][0])
        newfiles = [file for file in files if file not in current_files]
        for filename in newfiles:
            path_file = self.Dir.absoluteFilePath(filename)
            file_ctime = datetime.fromtimestamp(os.path.getctime(path_file))
            message = f"File {path_file} has add been!\n Time created: {file_ctime}"
            self.AddNewFile(filename, path_file, message)
            

    def GetContentFile(self, filename):
        for i in range(len(self.files_and_contents)):
            if self.files_and_contents[i][0] == filename:
                content = self.files_and_contents[i][1]
                return [content, i]
        return False
            
    
    def AddNewFile(self, file, path_file, msg):
        self.Status.addItem(msg)
        if os.path.isfile(path_file):
            content_file_public = self.ContentFileToSha256(path_file)
            list_files_attack = self.Dir_1.entryList()
            if file in list_files_attack:
                with open(self.Dir_1.absoluteFilePath(file), "rb") as f:
                    file_content = f.read()  
                    content_file_attack = hashlib.sha256(file_content).hexdigest()
                if (content_file_public != content_file_attack):
                    file_time = datetime.now().strftime("%d-%m-%y_%H-%M-%S-%f")
                    file_copied = os.path.join(self.AttackDir, file).replace(".txt", f"_{file_time}.txt") 
                else:
                    file_copied = os.path.join(self.AttackDir, file)
            else:
                file_copied = os.path.join(self.AttackDir, file)
            try:
                shutil.copyfile(path_file, file_copied)
            except:
                self.ShowStatus("Error!", "Copying files failed", False)
        self.ListFile.addItem(file)
        contentFile = self.ContentFileToSha256(path_file)
        self.files_and_contents.append([file, contentFile])
        self.watcher.addPath(path_file)

    def Watcher(self, directory):
        self.Attack.setEnabled(False)
        self.Finish.setEnabled(True)  
        self.paths = self.listFile(directory)
        self.paths.append(directory)
        self.watcher.addPaths(self.paths)
        self.ListFilesAndContent()
        self.watcher.fileChanged.connect(self.on_file_changed)
        self.watcher.directoryChanged.connect(self.on_directory_changed)
        self.CopyFileToAttackFolder()
        #print(self.files_and_contents)
    
    def ListFilesAndContent(self):
        current_files = self.Dir.entryList()
        current_files.remove('.')
        current_files.remove('..')
        content_files = []
        for file in current_files:
            path_file = "./public/" + file
            if os.path.isfile(path_file):
                contentToSha256 = self.ContentFileToSha256(path_file)
                content_files.append(contentToSha256)
            else:
                current_files.remove(file)
        for i in range(len(current_files)):
            self.files_and_contents.append([current_files[i], content_files[i]])

    def CopyFileToAttackFolder(self):
        for file in self.paths:
            if os.path.isfile(file):
                try:
                    file_copied = os.path.join(self.AttackDir, os.path.basename(file))
                    shutil.copyfile(file, file_copied)
                except:
                    self.ShowStatus("Error!", "Copying files failed", False)
                    return
        self.ShowStatus("Success!", "Copied files successfully!!!", True)

    def ContentFileToSha256(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                file_content = f.read()  #+ bytes(file_path, "utf-8")
                content = hashlib.sha256(file_content).hexdigest()

        return content
    
    def FinishWatcher(self):
        self.watcher.removePaths(self.paths)
        self.paths.clear()
        self.current_files.clear()
        self.Finish.setEnabled(False)
        self.Path.setEnabled(True)
    
    def ResetApp(self):
        self.SetDefaultApp()
        for i in range(self.ListFile.count()):
            self.ListFile.takeItem(0)
        for i in range(self.Status.count()):
            self.Status.takeItem(0)

    def SelectFiletoRead(self):
        widget = self.centralwidget
        source_file, _ = QFileDialog.getOpenFileName(widget, "Choose source file", self.AttackDir, "All Files (*)")
        self.File.setText(source_file)
        self.File.setWordWrap(True)
        self.Read.setEnabled(True)

    def ReadFileToClipBoard(self):
        path_file = self.File.text()
        if path_file and self.PublicDir:
            try:
                with open(path_file, "r") as f:
                    data = f.read()
                self.info.setText(data)
                self.info.setWordWrap(True)
                self.label_6.show()
                self.info.show()
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

    def SetDefaultApp(self):
        self.label_5.hide()
        self.Status.hide()
        self.label_6.hide()
        self.info.hide()
        self.File.setText('')
        self.Attack.setEnabled(True)
        self.Finish.setEnabled(False)
        self.Path.setEnabled(False)
        self.Read.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MAIN_HANDLE()
    MainWindow.show()
    sys.exit(app.exec_())
