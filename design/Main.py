# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 545)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.frameInput.setObjectName("frameInput")
        self.horizontalLayout.addWidget(self.frameInput)
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.decodeAsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.decodeAsComboBox.setEditable(False)
        self.decodeAsComboBox.setCurrentText("")
        self.decodeAsComboBox.setObjectName("decodeAsComboBox")
        self.horizontalLayout_2.addWidget(self.decodeAsComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 517, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.choise_system_node = QtGui.QAction(MainWindow)
        self.choise_system_node.setObjectName("choise_system_node")
        self.add_system_node = QtGui.QAction(MainWindow)
        self.add_system_node.setObjectName("add_system_node")
        self.change_system_node = QtGui.QAction(MainWindow)
        self.change_system_node.setObjectName("change_system_node")
        self.add_single_node = QtGui.QAction(MainWindow)
        self.add_single_node.setObjectName("add_single_node")
        self.action_TCP = QtGui.QAction(MainWindow)
        self.action_TCP.setObjectName("action_TCP")
        self.action_RTU = QtGui.QAction(MainWindow)
        self.action_RTU.setObjectName("action_RTU")
        self.action_Unix_Time = QtGui.QAction(MainWindow)
        self.action_Unix_Time.setObjectName("action_Unix_Time")
        self.menu_2.addAction(self.choise_system_node)
        self.menu_2.addAction(self.add_system_node)
        self.menu_2.addAction(self.change_system_node)
        self.menu_3.addAction(self.action_TCP)
        self.menu_3.addAction(self.action_RTU)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.add_single_node)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_Unix_Time)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyModbus"))
        self.label.setText(_translate("MainWindow", "?????????? (?????? crc):"))
        self.sendButton.setText(_translate("MainWindow", "??????????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????? ???????????????????????? ??????:"))
        self.menu.setTitle(_translate("MainWindow", "??????????"))
        self.menu_2.setTitle(_translate("MainWindow", "?????????????? ????????????"))
        self.menu_3.setTitle(_translate("MainWindow", "??????????"))
        self.choise_system_node.setText(_translate("MainWindow", "??????????????"))
        self.add_system_node.setText(_translate("MainWindow", "????????????????"))
        self.change_system_node.setText(_translate("MainWindow", "????????????????"))
        self.add_single_node.setText(_translate("MainWindow", "???????????????? ??????????????"))
        self.action_TCP.setText(_translate("MainWindow", "?????????????????? ???? TCP"))
        self.action_RTU.setText(_translate("MainWindow", "?????????????????? ???? RTU"))
        self.action_Unix_Time.setText(_translate("MainWindow", "?????????????????? Unix-Time"))
