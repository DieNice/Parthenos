from PyQt5 import QtWidgets
import sys

from gui.mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
