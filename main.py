from PyQt5 import QtWidgets
import sys

from PyQt5.QtCore import QDir, QModelIndex
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel

from gui.mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__drivesModel = QFileSystemModel()
        self.__filesModel = QFileSystemModel()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_dir.clicked.connect(self.adding_dir)
        self.ui.add_files.clicked.connect(self.adding_files)
        self.ui.actionAdd.triggered.connect(self.adding_files)
        self.ui.treeView.clicked.connect(self.treeViewClicked)

        sPath = "home/"
        drivesModel = QFileSystemModel(self)
        drivesModel.setFilter(QDir.NoDotAndDotDot | QDir.Dirs)
        drivesModel.setRootPath(sPath)
        self.ui.treeView.setModel(drivesModel)
        self.ui.treeView.hideColumn(1)
        self.ui.treeView.hideColumn(2)
        self.ui.treeView.hideColumn(3)

        filesModel = QFileSystemModel(self)
        filesModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)
        filesModel.setRootPath(sPath)
        self.ui.treeView.setModel(filesModel)

    def adding_dir(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.List)

        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        for i in fileNames:
            self.ui.listWidget.addItem(i)

    def adding_files(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setViewMode(QFileDialog.List)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        for i in fileNames:
            self.ui.listWidget.addItem(i)

    def treeViewClicked(self, index):
        sPath = self.__drivesModel.fileInfo(index).absolutePath()
        self.ui.treeView.setRootIndex(self.__filesModel.setRootPath(sPath))


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
