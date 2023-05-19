from PyQt6 import QtWidgets
from forms.connection_status_dialogs.connection_not_established_dialog.ConnectionNotEstablishedDesigner import Ui_ConnectionNotEstablished

class ConnectionNotEstabledForm(QtWidgets.QWidget, Ui_ConnectionNotEstablished):
    def __init__(self):
        super(ConnectionNotEstabledForm,self).__init__()
        self.setupUi(self)
        self.buttonBox.clicked.connect(lambda: self.close())
        
def show():
    ConnectionNotEstabledDialog = ConnectionNotEstabledForm()
    return ConnectionNotEstabledDialog.show