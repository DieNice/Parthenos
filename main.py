from PyQt5 import QtWidgets
import sys

from PyQt5.QtWidgets import QFileDialog

from gui.mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_dir.clicked.connect(self.adding_dir)
        self.ui.add_files.clicked.connect(self.adding_files)

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


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
