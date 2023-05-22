from PyQt6 import QtWidgets
import modules.jsonWorker as jsonWorker
from forms.comand_systems.AddCommand.AddCommandDesigner import Ui_AddButton
from forms.comand_systems.AddCommand.OkDialog.AddCommandOkForm import AddCommandOkDialog

data = jsonWorker.readFile()

class AddCommandForm(QtWidgets.QWidget, Ui_AddButton):
    def __init__(self):
        super(AddCommandForm, self).__init__()
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
        if not (cmdName == '') and not (cmdFrame == ''):
            for system in data:
                if system["systemName"] == systemName:
                    newComand = {"commandName": cmdName, "command": cmdFrame}
                    commands = system["commands"]
                    commands.append(newComand)
                    jsonWorker.writeFile(data)
                    self.showAddOk()
    
    def showAddOk(self):
        global dialog
        dialog = AddCommandOkDialog()
        dialog.show()