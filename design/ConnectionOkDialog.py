# Form implementation generated from reading ui file 'ConnectionOkDialog.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        ConnectionDialog.setObjectName("ConnectionDialog")
        ConnectionDialog.resize(170, 101)
        ConnectionDialog.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(ConnectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ConnectionDialog)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.OKButton = QtWidgets.QPushButton(ConnectionDialog)
        self.OKButton.setObjectName("OKButton")
        self.verticalLayout.addWidget(self.OKButton)

        self.retranslateUi(ConnectionDialog)
        QtCore.QMetaObject.connectSlotsByName(ConnectionDialog)

    def retranslateUi(self, ConnectionDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ConnectionDialog", "Подключение установленно"))
        self.OKButton.setText(_translate("ConnectionDialog", "ОК"))
