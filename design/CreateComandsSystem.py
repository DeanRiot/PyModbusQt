# Form implementation generated from reading ui file 'CreateComandsSystem.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateComandSystemForm(object):
    def setupUi(self, CreateComandSystemForm):
        CreateComandSystemForm.setObjectName("CreateComandSystemForm")
        CreateComandSystemForm.resize(402, 268)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateComandSystemForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CreateComandSystemForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.systemNameEdit = QtWidgets.QLineEdit(CreateComandSystemForm)
        self.systemNameEdit.setObjectName("systemNameEdit")
        self.horizontalLayout.addWidget(self.systemNameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(CreateComandSystemForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ComandNameEdit1 = QtWidgets.QLineEdit(CreateComandSystemForm)
        self.ComandNameEdit1.setObjectName("ComandNameEdit1")
        self.horizontalLayout_2.addWidget(self.ComandNameEdit1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(CreateComandSystemForm)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ComandValueEdit1 = QtWidgets.QLineEdit(CreateComandSystemForm)
        self.ComandValueEdit1.setObjectName("ComandValueEdit1")
        self.horizontalLayout_3.addWidget(self.ComandValueEdit1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(CreateComandSystemForm)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ComandNameEdit2 = QtWidgets.QLineEdit(CreateComandSystemForm)
        self.ComandNameEdit2.setObjectName("ComandNameEdit2")
        self.horizontalLayout_4.addWidget(self.ComandNameEdit2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(CreateComandSystemForm)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.ComandValueEdit2 = QtWidgets.QLineEdit(CreateComandSystemForm)
        self.ComandValueEdit2.setObjectName("ComandValueEdit2")
        self.horizontalLayout_5.addWidget(self.ComandValueEdit2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.CreateSystemButton = QtWidgets.QPushButton(CreateComandSystemForm)
        self.CreateSystemButton.setObjectName("CreateSystemButton")
        self.verticalLayout.addWidget(self.CreateSystemButton)

        self.retranslateUi(CreateComandSystemForm)
        QtCore.QMetaObject.connectSlotsByName(CreateComandSystemForm)

    def retranslateUi(self, CreateComandSystemForm):
        _translate = QtCore.QCoreApplication.translate
        CreateComandSystemForm.setWindowTitle(_translate("CreateComandSystemForm", "Создать систему команд"))
        self.label.setText(_translate("CreateComandSystemForm", "Название системы команд"))
        self.label_2.setText(_translate("CreateComandSystemForm", "Название команды"))
        self.label_3.setText(_translate("CreateComandSystemForm", "Команда"))
        self.label_4.setText(_translate("CreateComandSystemForm", "Название команды"))
        self.label_5.setText(_translate("CreateComandSystemForm", "Команда"))
        self.CreateSystemButton.setText(_translate("CreateComandSystemForm", "Создать систему команд"))