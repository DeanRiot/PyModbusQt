from PyQt6 import QtWidgets
from forms.connection_status_dialogs.connection_ok_dialog.ConnectionDialogDesigner import Ui_ConnectionDialog

class ConnectionOkDialog(QtWidgets.QWidget, Ui_ConnectionDialog):
    def __init__(self):
        super(ConnectionOkDialog, self).__init__()
        self.setupUi(self)
        self.label.setText("Подключение установлено")
        self.setWindowIconText("Статус")
        self.OKButton.clicked.connect(lambda :self.close())

def show():
    ConnOKStatusForm = ConnectionOkDialog()
    return ConnOKStatusForm.show
