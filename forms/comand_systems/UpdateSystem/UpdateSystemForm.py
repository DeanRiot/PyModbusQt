from PyQt6 import QtWidgets
from forms.comand_systems.UpdateSystem.UpdateComandDesigner import Ui_UpdateComandForm
import modules.jsonWorker as jsonWorker

data = jsonWorker.readFile()

class UpdateCommandsSystemForm(QtWidgets.QWidget, Ui_UpdateComandForm):
    def __init__(self):
        super(UpdateCommandsSystemForm, self).__init__()
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

def show():
    updateSystemForm = UpdateCommandsSystemForm()
    return updateSystemForm.show