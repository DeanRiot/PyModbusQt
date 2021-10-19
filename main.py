"""
TODO:
 - make rtu working on
 - implement some views form received data
 - crc smells like shit
"""

import sys  # sys нужен для передачи argv в QApplication
import asyncio

import modules.modb as modbus
import modules.TCPClient as TCPClient
import modules.jsonWorker as jsonWorker
import modules.dateTimeProcessing as dateTimeCalc
import modules.receiveProcessing as receiveProcessing

from PyQt6 import QtWidgets

import design.Main as mainForm
import design.TCPSettings as TCPSettingsForm
import design.RTUSettings as RTUSettingsForm
import design.ConnectionOkDialog as ConnectionOKDialog
import design.AddCommandForm as AddCommandForm
import design.AddCommandOkDialog as AddCommandOkDialog
import design.ChoiseComandForm as ChoiseCommandForm
import design.CreateComandsSystem as CreateCommandsSystemForm
import design.EditComandForm as EditCommandForm

data = jsonWorker.readFile()

MainForm = None
TcpConnection = None

class MainView(QtWidgets.QMainWindow, mainForm.Ui_MainWindow):
    global MainForm
    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        self.decodeAsComboBox.insertItems(0, ['hex', 'Ascii', 'dateTime'])
        self.action_TCP.triggered.connect(openTCPConnections)
        self.action_RTU.triggered.connect(openRTUConnections)
        self.sendButton.clicked.connect(self.sendFrame)
        self.add_single_node.triggered.connect(openAddCommand)
        self.choise_system_node.triggered.connect(openChoiseComand)
        self.action_Unix_Time.triggered.connect(self.calcTimestamp)
        self.add_system_node.triggered.connect(openAddCommandsSystem)
        self.change_system_node.triggered.connect(openChangeCommandsSystem)
        MainForm = self

    def sendFrame(self):
        if TcpConnection is not None:
            frameData = self.frameInput.text()
            frame = modbus.createFrame(modbus.parseHexFrame(frameData))
            data_bytes = bytes(frame)
            asyncio.run(TCPClient.SendFrame(data_bytes, TcpConnection, self))

    def calcTimestamp(self):
        self.frameInput.setText(dateTimeCalc.calcHex())


def openChangeCommandsSystem():
    global updateSystemForm
    updateSystemForm = UpdateCommandsSystemView()
    updateSystemForm.show()


def openAddCommandsSystem():
    global addCommandSystemsForm
    addCommandSystemsForm = CreateCommandsSystemView()
    addCommandSystemsForm.show()


def openChoiseComand():
    global ChoiseComand
    ChoiseComand = ChoiseComandView()
    ChoiseComand.show()

def openAddCommand():
    global AddCommand
    AddCommand = AddCommandView()
    AddCommand.show()


def openTCPConnections():
    global TCPConnView
    TCPConnView = TCPConnectionsView()
    TCPConnView.show()


def openRTUConnections():
    global RTUConnView
    RTUConnView = RTUConnectionsView()
    RTUConnView.show()


def showOKStatus():
    global ConnOKStatusForm
    ConnOKStatusForm = ConnectStatusDialog()
    ConnOKStatusForm.show()


class TCPConnectionsView(QtWidgets.QWidget, TCPSettingsForm.Ui_TCPSettings):
    def __init__(self):
        super(TCPConnectionsView, self).__init__()
        self.setupUi(self)
        self.connectButton.clicked.connect(self.onConnectionButtonClick)

    def onConnectionButtonClick(self):
        global TcpConnection
        if not(self.ip_edit.text() == '') and not(self.port_edit.text() == ''):
            try:
                ip = self.ip_edit.text()
                port = self.port_edit.text()
                TcpConnection = TCPClient.Connect(ip, int(port))
            except:
                TcpConnection = None
                self.showErrStatus()
            showOKStatus()


class RTUConnectionsView(QtWidgets.QWidget, RTUSettingsForm.Ui_RTUSettings):
    def __init__(self):
        super(RTUConnectionsView, self).__init__()
        self.setupUi(self)


class ConnectStatusDialog(QtWidgets.QWidget, ConnectionOKDialog.Ui_ConnectionDialog):
    def __init__(self):
        super(ConnectStatusDialog, self).__init__()
        self.setupUi(self)


class AddCommandView(QtWidgets.QWidget, AddCommandForm.Ui_AddButton):
    def __init__(self):
        super(AddCommandView, self).__init__()
        self.setupUi(self)
        systemsNames = []
        self.comboBox.clear()
        for systems in data:
            systemsNames.append(systems["systemName"])
        self.comboBox.insertItems(0, systemsNames)
        self.AddCommandButton.clicked.connect(self.onAddFrameClick)

    def onAddFrameClick(self):
        cmdName = self.lineEdit_2.text()
        cmdFrame = self.lineEdit.text()
        systemName = self.comboBox.currentText()
        if not(cmdName == '') and not(cmdFrame == ''):
            for system in data:
                if system["systemName"] == systemName:
                    newComand = {"commandName":cmdName, "command":cmdFrame}
                    commands = system["commands"]
                    commands.append(newComand)
                    jsonWorker.writeFile(data)
                    showAddOk()

def showAddOk():
    global AddCommandOkDialogForm
    AddCommandOkDialogForm = AddCommandOkDialogView()
    AddCommandOkDialogForm.show()


class AddCommandOkDialogView(QtWidgets.QWidget, AddCommandOkDialog.Ui_CommandAddDialog):
    def __init__(self):
        super(AddCommandOkDialogView, self).__init__()
        self.setupUi(self)


class ChoiseComandView(QtWidgets.QWidget, ChoiseCommandForm.Ui_ChoiseComandForm):
    def __init__(self):
        super(ChoiseComandView, self).__init__()
        self.setupUi(self)
        systemsNames = []
        comands = []
        self.systemsComboBox.clear()
        self.comandsComboBox.clear()
        for systems in data:
            systemsNames.append(systems["systemName"])
            for comandName in systems["commands"]:
                comands.append(comandName["commandName"])
        self.systemsComboBox.insertItems(0, systemsNames)
        self.comandsComboBox.insertItems(0, comands)
        self.ChoiseButton.clicked.connect(self.choiseComand)
        self.systemsComboBox.currentIndexChanged.connect(self.swapCommands)

    def choiseComand(self):
        for system in data:
            if system["systemName"] == self.systemsComboBox.currentText():
                for command in system["commands"]:
                    if command["commandName"] == self.comandsComboBox.currentText():
                        MainFormWindow.frameInput.setText(command["command"])
                        break

    def swapCommands(self):
        for system in data:
            if system["systemName"] == self.systemsComboBox.currentText():
                self.comandsComboBox.clear()
                for command in system["commands"]:
                    self.comandsComboBox.addItem(command["commandName"])




class CreateCommandsSystemView(QtWidgets.QWidget, CreateCommandsSystemForm.Ui_CreateComandSystemForm):
    def __init__(self):
        super(CreateCommandsSystemView, self).__init__()
        self.setupUi(self)
        self.CreateSystemButton.clicked.connect(self.onCreateSystemClicked)

    def onCreateSystemClicked(self):
        sysName = self.systemNameEdit.text()
        frameName1 = self.ComandNameEdit1.text()
        frameValue1 = self.ComandValueEdit1.text()
        frameName2 = self.ComandNameEdit2.text()
        frameValue2 = self.ComandValueEdit2.text()
        if sysName != '' and frameName1!='' and frameValue1 != '' and frameName2 !='' and frameValue2 != '':
            system = {"systemName":sysName,
                      "commands":[
                          {"commandName":frameName1, "command":frameValue1},
                          {"commandName": frameName2, "command": frameValue2}]}
            data.append(system)
            print(data)
            jsonWorker.writeFile(data)
            showAddOk()


class UpdateCommandsSystemView(QtWidgets.QWidget, EditCommandForm.Ui_EditComandForm):
    def __init__(self):
        super(UpdateCommandsSystemView, self).__init__()
        self.setupUi(self)
        systemsNames = []
        comands = []
        for systems in data:
            systemsNames.append(systems["systemName"])
            for comandName in systems["commands"]:
                comands.append(comandName["commandName"])
        self.systemsComboBox.insertItems(0, systemsNames)
        self.comandsComboBox.insertItems(0, comands)
        self.systemsComboBox.currentIndexChanged.connect(self.swapCommands)
        self.comandsComboBox.currentIndexChanged.connect(self.choiseCommand)
        self.editComandButton.clicked.connect(self.onFrameEditClick)

    def choiseCommand(self):
        for system in data:
            if system["systemName"] == self.systemsComboBox.currentText():
                for command in system["commands"]:
                    if command["commandName"] == self.comandsComboBox.currentText():
                        self.comandValue.setText(command["command"])
                        break

    def swapCommands(self):
        for system in data:
            if system["systemName"] == self.systemsComboBox.currentText():
                self.comandsComboBox.clear()
                for command in system["commands"]:
                    self.comandsComboBox.addItem(command["commandName"])

    def onFrameEditClick(self):
        for system in data:
            if system["systemName"] == self.systemsComboBox.currentText():
                for cmd in system['commands']:
                    if cmd["commandName"] == self.comandsComboBox.currentText():
                        cmd.update({"command": self.comandValue.text()})
        jsonWorker.writeFile(data)


def getMainForm():
    return MainForm()

def main():
    global MainFormWindow
    app = QtWidgets.QApplication(sys.argv)
    MainFormWindow = MainView()
    MainFormWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
