from PyQt6 import QtWidgets
from forms.comand_systems.ChoiseComand.ChoiseComandDesigner import Ui_ChoiseComandForm
import modules.jsonWorker as jsonWorker

data = jsonWorker.readFile()
class ChoiseComandForm(QtWidgets.QWidget, Ui_ChoiseComandForm):
    def __init__(self):
        super(ChoiseComandForm, self).__init__()
        self.setupUi(self)
        systemsNames = []
        comands = []
        self.systemsComboBox.clear()
        self.comandsComboBox.clear()
        for systems in data:
            systemsNames.append(systems["systemName"])
            for comandName in systems["commands"]:
                comands.append(comandName["commandName"])
        self.systemsComboBox.insertItems(0, systemsNames)
        self.comandsComboBox.insertItems(0, comands)
        self.ChoiseButton.clicked.connect(self.choiseComand)
        self.systemsComboBox.currentIndexChanged.connect(self.swapCommands)

    def choiseComand(self):
        for system in data:
            if system["systemName"] == self.systemsComboBox.currentText():
                for command in system["commands"]:
                    if command["commandName"] == self.comandsComboBox.currentText():
                        self.output.setText(command["command"])
                        break

    def swapCommands(self):
        for system in data:
            if system["systemName"] == self.systemsComboBox.currentText():
                self.comandsComboBox.clear()
                for command in system["commands"]:
                    self.comandsComboBox.addItem(command["commandName"])


def show():
    ChoiseComand = ChoiseComandForm()
    return ChoiseComand.show