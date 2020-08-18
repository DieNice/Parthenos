# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 391))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 751, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.add_files = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_files.setObjectName("add_files")
        self.gridLayout.addWidget(self.add_files, 0, 1, 1, 1)
        self.add_dir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_dir.setObjectName("add_dir")
        self.gridLayout.addWidget(self.add_dir, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.goto_archive = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.goto_archive.setObjectName("goto_archive")
        self.gridLayout.addWidget(self.goto_archive, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.add_to_index = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_to_index.setObjectName("add_to_index")
        self.horizontalLayout.addWidget(self.add_to_index)
        self.treeView = QtWidgets.QTreeView(self.verticalLayoutWidget)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(False)
        self.tab_2.setMouseTracking(False)
        self.tab_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(False)
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 410, 781, 111))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOperations = QtWidgets.QMenu(self.menubar)
        self.menuOperations.setObjectName("menuOperations")
        self.menuParameters = QtWidgets.QMenu(self.menubar)
        self.menuParameters.setObjectName("menuParameters")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionFind_Action = QtWidgets.QAction(MainWindow)
        self.actionFind_Action.setObjectName("actionFind_Action")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionGetting_started = QtWidgets.QAction(MainWindow)
        self.actionGetting_started.setObjectName("actionGetting_started")
        self.actionKeymap_referance = QtWidgets.QAction(MainWindow)
        self.actionKeymap_referance.setObjectName("actionKeymap_referance")
        self.actionRegistre = QtWidgets.QAction(MainWindow)
        self.actionRegistre.setObjectName("actionRegistre")
        self.actionCheck_for_updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose_pickling = QtWidgets.QAction(MainWindow)
        self.actionClose_pickling.setObjectName("actionClose_pickling")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionAdd.setObjectName("actionAdd")
        self.actionextract = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/extract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionextract.setIcon(icon1)
        self.actionextract.setObjectName("actionextract")
        self.actionsend = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsend.setIcon(icon2)
        self.actionsend.setObjectName("actionsend")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionClose_pickling)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionFind_Action)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionGetting_started)
        self.menuHelp.addAction(self.actionKeymap_referance)
        self.menuHelp.addAction(self.actionRegistre)
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuHelp.addAction(self.actionabout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOperations.menuAction())
        self.menubar.addAction(self.menuParameters.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionextract)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionsend)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Parthenos"))
        self.add_files.setText(_translate("MainWindow", "add files"))
        self.add_dir.setText(_translate("MainWindow", "add directory"))
        self.goto_archive.setText(_translate("MainWindow", "Go to Archiving files"))
        self.add_to_index.setText(_translate("MainWindow", "add to index"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "File selection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Archiving files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "File upload"))
        self.menuFile.setTitle(_translate("MainWindow", "F&ile"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Commands"))
        self.menuOperations.setTitle(_translate("MainWindow", "Oper&ations"))
        self.menuParameters.setTitle(_translate("MainWindow", "&Parameters"))
        self.menuHelp.setTitle(_translate("MainWindow", "He&lp"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "&New pickling..."))
        self.actionClose.setText(_translate("MainWindow", "&Open pickling..."))
        self.actionFind_Action.setText(_translate("MainWindow", "&Find Action"))
        self.actionHelp.setText(_translate("MainWindow", "&Help"))
        self.actionGetting_started.setText(_translate("MainWindow", "&Getting started"))
        self.actionKeymap_referance.setText(_translate("MainWindow", "&Keymap reference"))
        self.actionRegistre.setText(_translate("MainWindow", "&Registre"))
        self.actionCheck_for_updates.setText(_translate("MainWindow", "&Check for updates"))
        self.actionabout.setText(_translate("MainWindow", "&about"))
        self.actionSave_As.setText(_translate("MainWindow", "&Save As"))
        self.actionClose_pickling.setText(_translate("MainWindow", "&Close pickling"))
        self.actionSettings.setText(_translate("MainWindow", "Sett&ings"))
        self.actionPrint.setText(_translate("MainWindow", "&Print"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionAdd.setToolTip(_translate("MainWindow", "<html><head/><body><p>ADD</p></body></html>"))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionextract.setText(_translate("MainWindow", "extract"))
        self.actionextract.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionsend.setText(_translate("MainWindow", "send"))
        self.actionsend.setToolTip(_translate("MainWindow", "<html><head/><body><p>Send</p></body></html>"))
import gui.res_rc
