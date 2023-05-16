import view.TCPSettings as TCPSettingsForm
import modules.TCPClient as TCPClient

class TCPConnectionsView(QtWidgets.QWidget, TCPSettingsForm.Ui_TCPSettings):
    def __init__(self):
        super(TCPConnectionsView, self).__init__()
        self.setupUi(self)
        self.connectButton.clicked.connect(self.onConnectionButtonClick)

    def onConnectionButtonClick(self):
        global TcpConnection
        if not (self.ip_edit.text() == '') and not (self.port_edit.text() == ''):
            try:
                ip = self.ip_edit.text()
                port = self.port_edit.text()
                rd_timeout = int(self.send_timeout_edit.text())
                defaut_timeout = int(self.receive_timeout_edit.text())
                TcpConnection = TCPClient.Connect(ip, int(port),rd_timeout, defaut_timeout)
                showOKStatus()
            except Exception as e:
                TcpConnection = None
                print(str(e))
                showErrStatus()

def showOKStatus():
    global ConnOKStatusForm
    ConnOKStatusForm = ConnectStatusDialog()
    ConnOKStatusForm.show()

def showErrStatus():
    global ConnErrStatusForm
    ConnErrStatusForm = ConnectErrStatusDialog()
    ConnErrStatusForm.show()