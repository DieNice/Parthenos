from PyQt5 import QtWidgets
import sys

from PyQt5.QtCore import QDir, QModelIndex
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QListWidgetItem

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

        # initialization treeView drivers
        sPath = "/home"
        # drivesModel.setFilter(QDir.NoDotAndDotDot | QDir.Dirs)
        self.__drivesModel.setRootPath(sPath)
        self.ui.treeView.setModel(self.__drivesModel)
        self.ui.treeView.hideColumn(1)
        self.ui.treeView.hideColumn(2)
        self.ui.treeView.hideColumn(3)

        # filesModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)
        self.__filesModel.setRootPath(sPath)
        self.ui.treeView.setModel(self.__filesModel)

        self.ui.treeView.clicked.connect(self.treeViewClicked)
        self.ui.add_to_index.clicked.connect(self.addingIndex)

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
        # sPath = self.__drivesModel.fileInfo(index).absolutePath()
        # self.ui.treeView.setRootIndex(self.__filesModel.setRootPath(sPath))
        pass

    def addingIndex(self):

        selecteditem = self.ui.treeView.currentIndex()
        mystr = self.__filesModel.filePath(selecteditem)
        self.ui.textEdit.setText(mystr)
        self.ui.listWidget.addItem(mystr)


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
