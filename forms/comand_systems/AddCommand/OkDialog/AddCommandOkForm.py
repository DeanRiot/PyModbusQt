from PyQt6 import QtWidgets
from forms.comand_systems.AddCommand.OkDialog.AddCommandOkDesigner import Ui_CommandAddDialog

class AddCommandOkDialog(QtWidgets.QWidget, Ui_CommandAddDialog):
    def __init__(self):
        super(AddCommandOkDialog, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.close())