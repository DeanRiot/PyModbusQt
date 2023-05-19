from PyQt6 import QtWidgets
from forms.main.MainFormDesigner import Ui_MainWindow
from forms.scripting.ScriptingForm import ScriptingForm
from forms.communicaton_settings.RTUSettings.RTUSettingsForm import RTUConnectionsForm
from forms.communicaton_settings.TCPSettings.TCPSettingsForm import TCPConnectionsForm
from forms.comand_systems.AddCommand.AddCommandForm import AddCommandForm
from forms.comand_systems.ChoiseComand.ChoiseComandForm import ChoiseComandForm
from forms.comand_systems.CreateSystem.CreateCommandsForm import CreateCommandsSystemForm
from forms.comand_systems.UpdateSystem.UpdateSystemForm import UpdateCommandsSystemForm
from forms.connection_status_dialogs.connection_not_established_dialog.ConnectionNotEstablishedDialog import ConnectionNotEstabledForm

from controller.sender import FrameSender
from modules.dateTimeProcessing import calcHex

class MainView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        self.decodeAsComboBox.insertItems(0, ['hex', 'Ascii', 'dateTime'])
        self.setupForms()
        self.setupCallbacks()
    
    def setupForms(self):
        self.RTUConnectionsForm = RTUConnectionsForm()
        self.TCPConnectionsForm = TCPConnectionsForm()
        self.AddCommandForm = AddCommandForm()
        self.ChoiseComandForm = ChoiseComandForm()
        self.CreateCommandsSystemForm = CreateCommandsSystemForm()
        self.UpdateCommandsSystemForm = UpdateCommandsSystemForm()
        self.ConnectionNotEstabledForm = ConnectionNotEstabledForm()

    def setupCallbacks(self):
        self.action_TCP.triggered.connect(self.TCPConnectionsForm.show)
        self.action_RTU.triggered.connect(self.RTUConnectionsForm.show)
        self.add_single_node.triggered.connect(self.AddCommandForm.show)
        self.choise_system_node.triggered.connect(self.ChoiseComandForm.show)
        self.add_system_node.triggered.connect(self.CreateCommandsSystemForm.show)
        self.change_system_node.triggered.connect(self.UpdateCommandsSystemForm.show)
        self.action_scripting.triggered.connect(self.showScriptingForm)
        self.action_Unix_Time.triggered.connect(self.calcTimestamp)

        self.sendButton.clicked.connect(self.sendFrame) 

    def sendFrame(self):
        TCPConnect = self.TCPConnectionsForm.TCPClient
        f_sender = FrameSender(TCPConnect)
        frameData = self.frameInput.text()
        out_repr = self.decodeAsComboBox.currentText()
        data = f_sender.sendAndReceive(frameData, out_repr)
        if not data.status: 
            self.ConnectionNotEstabledForm.show()
            return
        self.listWidget.addItem(data.request)
        self.listWidget.addItem(data.response)

    def calcTimestamp(self):
        self.frameInput.setText(calcHex())
    
    def showScriptingForm(self):
        TCPConnect = self.TCPConnectionsForm.TCPClient
        f_sender = FrameSender(TCPConnect)
        global Form
        Form = ScriptingForm(f_sender)
        Form.show()