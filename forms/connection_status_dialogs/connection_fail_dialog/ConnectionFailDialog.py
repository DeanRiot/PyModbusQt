from PyQt6 import QtWidgets
from forms.connection_status_dialogs.connection_fail_dialog.ConnectionDialogDesigner import Ui_ConnectionDialog

class ConnectionFailDialog(QtWidgets.QWidget, Ui_ConnectionDialog):
    def __init__(self):
        super(ConnectionFailDialog, self).__init__()
        self.setupUi(self)
        self.label.setText("Ошибка подключения")
        self.setWindowIconText("Ошибка")
        self.OKButton.clicked.connect(lambda: self.close())

def show():
    ConnErrStatusForm = ConnectionFailDialog()
    return ConnErrStatusForm.show