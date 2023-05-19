from PyQt6 import QtWidgets
from forms.communicaton_settings.TCPSettings.TCPSettingsDesigner import Ui_TCPSettings
from modules.TCPClient import TCPClient
from forms.connection_status_dialogs.connection_ok_dialog.ConnectionOkDialog import ConnectionOkDialog
from forms.connection_status_dialogs.connection_fail_dialog.ConnectionFailDialog import ConnectionFailDialog 

class TCPConnectionsForm(QtWidgets.QWidget, Ui_TCPSettings):
    def __init__(self):
        super(TCPConnectionsForm, self).__init__()
        self.setupUi(self)
        self.connectButton.clicked.connect(self.onConnectionButtonClick)
        self.setupForms()
        self.TCPClient = TCPClient()
    
    def setupForms(self):
        self.ConnectionFailDialog = ConnectionFailDialog()
        self.ConnectionOkDialog = ConnectionOkDialog()
    
    def onConnectionButtonClick(self):
        global TcpConnection
        if not (self.ip_edit.text() == '') and not (self.port_edit.text() == ''):
            try:
                ip = self.ip_edit.text()
                port = self.port_edit.text()
                rd_timeout = int(self.send_timeout_edit.text())
                defaut_timeout = int(self.receive_timeout_edit.text())
                TcpConnection = self.TCPClient.Connect(ip, int(port),rd_timeout, defaut_timeout)
                self.ConnectionOkDialog.show()
            except Exception as e:
                TcpConnection = None
                print(str(e))
                self.ConnectionFailDialog.show()

def show():
    tcpConnectionForm = TCPConnectionsForm() 
    return tcpConnectionForm.show