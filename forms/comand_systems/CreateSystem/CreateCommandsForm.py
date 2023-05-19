from PyQt6 import QtWidgets
from forms.comand_systems.CreateSystem.CreateComandSystemFormDesiger import Ui_CreateComandSystemForm
from forms.comand_systems.AddCommand.OkDialog.AddCommandOkForm import AddCommandOkDialog
import modules.jsonWorker as jsonWorker

data = jsonWorker.readFile()

class CreateCommandsSystemForm(QtWidgets.QWidget, Ui_CreateComandSystemForm):
    def __init__(self):
        super(CreateCommandsSystemForm, self).__init__()
        self.setupUi(self)
        self.CreateSystemButton.clicked.connect(self.onCreateSystemClicked)

    def onCreateSystemClicked(self):
        sysName = self.systemNameEdit.text()
        frameName1 = self.ComandNameEdit1.text()
        frameValue1 = self.ComandValueEdit1.text()
        frameName2 = self.ComandNameEdit2.text()
        frameValue2 = self.ComandValueEdit2.text()
        if sysName != '' and frameName1 != '' and frameValue1 != '' and frameName2 != '' and frameValue2 != '':
            system = {"systemName": sysName,
                      "commands": [
                          {"commandName": frameName1, "command": frameValue1},
                          {"commandName": frameName2, "command": frameValue2}]}
            data.append(system)
            jsonWorker.writeFile(data)
            showAddOk()
    
        def showAddOk(self):
            global dialog
            dialog = AddCommandOkDialog()
            dialog.show()